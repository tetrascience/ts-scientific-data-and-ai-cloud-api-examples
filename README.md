# ts-scientific-data-cloud-api-examples
TetraScience Scientific Data Cloud API Usage Examples

## Getting started

* Install Python 3.8 or higher (We recommend using pyenv if you have to work with multiple versions on the same machine.)
* Install [Poetry](https://python-poetry.org/docs/) for dependency management and packaging in Python.
* Install [Jupyter Notebook](https://jupyter.org/install)

## Overview

Our [Public API](https://developers.tetrascience.com/reference/introduction-1) provides methods to get information about data acquisition (Agents), get information about files stored in the data lake, search through and modify files in the data lake, and programmatically create and execute data pipelines.

While these APIs provide access to the platform, there exist some common use patterns across customers documented in this repo. Additional use cases can be created by leveraging the APIs in systematic fashions and this repo is designed to get you started using the APIs and give you a sense of what you can accomplish.

Current Examples in this repo:

* [Loading Authentication File](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/Loading%20Authentication%20File.ipynb)
* [TetraScience Scientific Data Cloud Configuration Report](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/TetraScience%20Scientific%20Data%20Cloud%20Configuration%20Report.ipynb)
* [Migrating Pipelines between Platform Instances](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/Migrating%20Pipelines%20between%20Platform%20Instances.ipynb)
* [Pulling IDS Data Cubes into Pandas DataFrame (Cytometry Example)](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/Pulling%20IDS%20Data%20Cubes%20into%20Pandas%20DataFrame%20(Cytometry%20Example).ipynb)
* [Data Synchronization](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/Data%20Synchronization.ipynb)
* [Retrieve IDS Field Descriptions](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/Retrieve%20IDS%20Field%20Descriptions.ipynb)
* [Querying Chromeleon Data](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/Querying%20Chromeleon%20Data.ipynb)
* [Querying Unicorn Data](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/Querying%20UNICORN%20Data.ipynb)
* [Finding Pipelines with Available Updates](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/examples/Finding%20Pipelines%20with%20Available%20Updates.ipynb)

## Contribute

We welcome contributions from the community that document the use of our APIs to accelerate scientific workflows. [Here are more details on how to contribute.](https://github.com/tetrascience/ts-scientific-data-cloud-api-examples/blob/main/Contributing.md)

## Disclaimer

The example notebooks in this repository are not fully supported product features. They are example use cases to demonstrate the capabilitiy of TetraScience's APIs. You are responsible for any code maintenance, deployment, and validation using these examples.
