"""
This script automates the process of downloading data from the WHO Global Tuberculosis Programme website.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import os

# Path to the you're Desired Brower's WebDriver..
edge_driver_path = r'C:\msedgedriver.exe'

# URL of the WHO's Global Tuberculosis Programme data page..
url = "https://www.who.int/teams/global-tuberculosis-programme/data"

# Path to save the downloaded file..
download_directory = r'C:\Users\Admin\Desktop\InternCareer'

# Initialize Edge driver with download directory..
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
