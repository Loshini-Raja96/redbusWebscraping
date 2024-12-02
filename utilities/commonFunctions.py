import os
import sys
sys.modules.pop('pandas', None)
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# This function returns a new WebDriver instance for selenium
# This line initializes a new WebDriver instance for Chrome, essentially starting a new Chrome browser session
def initialize_driver(): 
    browser = webdriver.Chrome() 
    browser.maximize_window()
    return browser

# driver---->selenium webdriver instance which is used to interact with browsers
# This function is used to load webpage using selenium's webdriver
# This command instructs the webdriver to open the specified url in the browser
def load_page(driver,url): 
    driver.get(url)         
    time.sleep(5)  

# Function to scrape bus routes
# by passing driver as argument to reuse an existing webdriver instance
def scrape_bus_routes(driver): 
    route_elements = driver.find_elements(By.CLASS_NAME, 'route')
    bus_routes_link = [route.get_attribute('href') for route in route_elements]
    bus_routes_name = [route.text.strip() for route in route_elements]
    return bus_routes_link, bus_routes_name

# Convert the list of dictionaries to a DataFrame
# Ensure the folder exists, or create it  
 # Combine folder path and file name 
 # Save the DataFrame to a CSV file
def exportCsv(bus_details,fileName):
    folderPath='../exportedCsvFiles'
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    file_path = os.path.join(folderPath,fileName)
    df = pd.DataFrame(bus_details)
    df.to_csv(file_path, index=False)
