"""
This script automates the process of downloading data from the WHO Global Tuberculosis Programme website
and performs various data processing techniques on the downloaded data.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import os
import pandas as pd

def download_data(url, download_directory):
    """
    Downloads the data from the given URL and saves it to the specified directory.

    Parameters:
        url (str): The URL of the webpage to download the data from.
        download_directory (str): The directory where the downloaded file will be saved.
    """
    # Initialize Edge driver with download directory
    options = webdriver.EdgeOptions()
    prefs = {"download.default_directory": download_directory}
    options.add_experimental_option("prefs", prefs)

    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=options)

    # Open the URL in the browser
    driver.get(url)

    # Find the download link based on the href attribute value
    download_link = driver.find_element(By.CSS_SELECTOR, "a[href*='generateCSV.asp']")

    # Click on the download link
    download_link.click()

    # Wait for the download to complete (adjust the time.sleep duration as needed)
    time.sleep(5)

    # Close the browser
    driver.quit()

def data_processing(csv_file_path, output_directory):
    """
    Performs various data processing techniques on the downloaded CSV file.

    Parameters:
        csv_file_path (str): The path to the downloaded CSV file.
        output_directory (str): The directory where the processed data will be saved.
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df.head())

    # Data processing techniques
    # 1. Handling Missing Values
    # Drop rows with any missing values
    processed_df = df.dropna()

    # 2. Data Transformation
    # Convert string columns to lowercase
    string_columns = df.select_dtypes(include=['object']).columns
    df[string_columns] = df[string_columns].apply(lambda x: x.str.lower())

    # 3. Data Aggregation
    # Group by 'country' and calculate the mean of numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    aggregated_df = df.groupby('country')[numeric_columns].mean().reset_index()
    
    # 4. Data Filtering
    # Filter rows based on a condition
    filtered_df = df[df['m_01'] > 100]  # Example condition, replace with appropriate column and condition

    # Display the processed DataFrames
    print("\nProcessed DataFrames:")
    print("Processed DataFrame with missing values removed:")
    print(processed_df.head())

    print("\nProcessed DataFrame with string columns converted to lowercase:")
    print(df.head())

    print("\nAggregated DataFrame with mean values per country:")
    print(aggregated_df.head())

    print("\nFiltered DataFrame with 'm_01' greater than 100:")
    print(filtered_df.head())

    # Save the processed DataFrames to CSV files
    processed_df.to_csv(os.path.join(output_directory, 'processed_data.csv'), index=False)
    aggregated_df.to_csv(os.path.join(output_directory, 'aggregated_data.csv'), index=False)
    filtered_df.to_csv(os.path.join(output_directory, 'filtered_data.csv'), index=False)

if __name__ == "__main__":
    # Path to the desired browser's WebDriver
    edge_driver_path = r'C:\msedgedriver.exe'

    # URL of the WHO's Global Tuberculosis Programme data page
    url = "https://www.who.int/teams/global-tuberculosis-programme/data"

    # Path to save the downloaded file
    download_directory = r'C:\Users\Admin\Desktop\InternCareer'

    # Path to save the processed data
    output_directory = r'C:\Users\Admin\Desktop\InternCareer'

    # Download data
    download_data(url, download_directory)

    # List all files in the download directory
    files = os.listdir(download_directory)

    # Filter files to find the CSV file based on the file extension or part of the filename
    csv_files = [file for file in files if file.endswith('.csv')]

    # Check if any CSV files were found
    if csv_files:
        # Assuming there's only one CSV file, use the first one found
        csv_filename = csv_files[0]
        csv_file_path = os.path.join(download_directory, csv_filename)

        # Perform data processing
        data_processing(csv_file_path, output_directory)
    else:
        print("No CSV files found in the download directory.")
