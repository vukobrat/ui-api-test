# Symphony Testing Framework
[![Python application](https://github.com/vukobrat/ui-api-test/actions/workflows/python-app.yml/badge.svg)](https://github.com/vukobrat/ui-api-test/actions/workflows/python-app.yml)
## Introduction

Welcome to the testing framework developed for Symphony, 
a Python-based framework for testing both UI and API components. 
This framework is built using pytest and Selenium and follows industry best practices for testing and test automation, using
Page Object and Page Factory patterns with Allure package for reporting.


## Project Structure
Here's an overview of the project structure:

- **config:** Contains configuration files, such as config.py, which holds endpoint URLs for both production and staging environments.

- **src:** The source code for the testing framework, including page objects for different web pages.

- **test-data:** Contains YAML files with expected data for UI testing.

- **tests:** The main directory for test cases, divided into api and ui folders. The common folder under both api and ui contains shared utility functions.

- **requirements.txt:** Lists the project dependencies, including Selenium, pytest, requests, Faker, and others.

- **pytest.ini:** Configuration file for pytest, specifying test file patterns and markers.

- **conftest.py:** Contains fixture definitions for setting up and tearing down the test environment.


## Prerequisites
**Host:** MacOS, Chrome browser

1. Create a virtual environment using a tool you prefer. In this example, I am using Anaconda [Installation Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html):
   - `conda create -n symph-ui python=3.11`

2. Download the desired driver [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/):
   - Navigate to the Downloads directory:
      - `mv chromedriver /usr/local/bin`
      - `sudo chmod +x /usr/local/bin/chromedriver`



## Installation

1. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Run All Tests

Run tests using Pytest:

```bash
pytest
```

### API Tests

Run API tests using Pytest marker:

```bash
pytest -m api
```

### UI Tests

Run UI tests using Pytest marker:

```bash
pytest -m ui
```

### Reports

After test run is finished, test results(JSON files) are stored into
*results* folder. 

To generate reports manually use bellow command and check 
created *reports* folder:

```bash
allure generate results -o reports 
```

### Docker run

Run tests into docker container:

```bash
docker build -t test_demo .
``` 
```bash
docker run -it test_demo (Note: use --rm flag if you want to remove container automatically after tests are finished)
```

Additionally, you can inspect desired container with :
```bash
docker run -it test_demo /bin/bash
``` 

## Test Plans
### UI
[UI Test Plan](https://belgradesurf.atlassian.net/wiki/external/YjI3NjcwOWZhY2U0NDYyZDhhZDY0MjBmYjJjMmI0NWI)

### API
[API Test Plan](https://belgradesurf.atlassian.net/wiki/external/ZDRhMjMyMGE5MTZlNDY1ZTk5NjAyMzQ4ODYxOGEzNDg)
### Test Overview
[Test Overview](https://belgradesurf.atlassian.net/wiki/external/NTE0MTUyN2U2NzVmNDZkNmJkMzNmMjBiNGNiNzI3NWQ)

