# WHO Global Tuberculosis Programme Data Scraper and Processor

This repository contains a Python script that automates the process of downloading data from the WHO Global Tuberculosis Programme website and performs basic data processing techniques on the downloaded data.

## Overview

The script utilizes Selenium, a web automation tool, to navigate to the WHO Global Tuberculosis Programme data page and download the data in CSV format. It then processes the downloaded CSV file using pandas, a powerful data manipulation library in Python, to perform the following data processing techniques:

1. **Handling Missing Values**: Drops rows with any missing values.
2. **Data Transformation**: Converts string columns to lowercase.
3. **Data Aggregation**: Groups data by country and calculates the mean of numeric columns.
4. **Data Filtering**: Filters rows based on a condition.

The processed data is then saved as separate CSV files in the specified output directory.

## Prerequisites

To run the script, you need the following:

- Python 3.x installed on your system.
- The necessary Python packages installed: `selenium`, `pandas`.
- WebDriver installed and its path configured in the script.

## Usage

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:
    ```
    pip install -r requirements.txt
    ```
3. Configure the path to the WebDriver in the script
4. Run the script `web_scraping.py`.
5. The processed data will be saved as CSV files in the specified output directory.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [pandas](https://pandas.pydata.org/)
- [WHO Global Tuberculosis Programme](https://www.who.int/teams/global-tuberculosis-programme/data)

Feel free to contribute to this project by opening issues or pull requests!

## 🚀 About Me
I'm a full stack Web & App Developer and an undergrad Data Science Student 👨‍💻🙌



## Authors

- [@Fahad](https://github.com/SyedFahad7)

