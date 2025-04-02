import asyncio
import json
from pathlib import Path

import aiohttp
from aiohttp_retry import RetryClient, RandomRetry


async def retrieve_presigned_url(
    client: aiohttp.ClientSession, api_url: str, file_id: str
) -> str:
    """Retrieve S3 pre-signed url from TDP

    Args:
        session: aiohttp client session
        api_url: TDP API URL
        file_id: TDP file identifier

    Returns:
        S3 pre-signed url
    """
    url = api_url + "datalake/retrieve"
    params = {"fileId": file_id, "getPresigned": "True"}
    async with client.get(url, params=params) as response:
        contents = await response.json()
        return contents["url"]


async def download_task(
    client: aiohttp.ClientSession, api_url: str, file_id: str
) -> bytes:
    """Download a TDP file from S3 by first retrieving an S3
    pre-signed URL, and then downloading the file from S3.

    Args:
        client: aiohttp client session
        api_url: TDP API URL
        file_id: TDP file id

    Returns:
        file contents
    """
    url = await retrieve_presigned_url(client, api_url, file_id)
    async with client.get(url) as response:
        return await response.read()


def bulk_file_download(file_ids: list[str], auth: dict, concurrency: int):
    """Download a collection of files from TDP asynchronously

    Args:
        file_ids: list of TDP fileIds to download
        auth: dict with TDP authentication data
        concurrency: maximum number of concurrent connections

    Returns:
        A list of file contents
    """

    # We wrap the async part of the function such that we can run it with
    # asyncio.run
    async def _bulk_file_download(api_url: str, auth_headers: dict):
        retry_options = RandomRetry(
            attempts=3, statuses=[502], min_timeout=0.1, max_timeout=3
        )
        conn = aiohttp.TCPConnector(limit=concurrency)

        async with RetryClient(
            retry_options=retry_options,
            headers=auth_headers,
            connector=conn,
        ) as client:
            tasks = [download_task(client, api_url, fid) for fid in file_ids]
            return await asyncio.gather(*tasks)

    # Unpack the auth object
    auth_headers = {"x-org-slug": auth["org"], "ts-auth-token": auth["auth_token"]}
    api_url = auth["api_url"]

    # Run event loop
    return asyncio.run(_bulk_file_download(api_url, auth_headers))


def search_file_ids():
    """This is a dummy function to search for files on TDP

    Implement your own logic to search for TDP files here.
    """
    return [
        "d51abcdc-04fd-40f8-9556-27a7add9a342",
        "ff807173-587d-40c6-88e7-7ca31522b71b",
        "eb4f967f-9547-4575-810b-2d263244cd34",
    ]


def main():
    """Application main function"""
    auth = json.loads(Path("auth.json").read_text())

    file_ids = search_file_ids()
    files = bulk_file_download(file_ids, auth=auth, concurrency=1)
    return files


if __name__ == "__main__":
    main()
