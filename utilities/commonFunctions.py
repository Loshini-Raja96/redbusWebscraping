from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# This function returns a new WebDriver instance for selenium
# This line initializes a new WebDriver instance for Chrome, essentially starting a new Chrome browser session
def initialize_driver(): 
    driver = webdriver.Chrome() 
    driver.maximize_window()
    return driver

# driver---->selenium webdriver instance which is used to interact with browsers
def load_page(driver,url): # This function is used to load webpage using selenium's webdriver
    driver.get(url)         # This command instructs the webdriver to open the specified url in the browser
    time.sleep(5)  # Wait for the page to load

# Function to scrape bus routes
def scrape_bus_routes(driver): # by passing driver as argument to reuse an existing webdriver instance
    route_elements = driver.find_elements(By.CLASS_NAME, 'route')
    bus_routes_link = [route.get_attribute('href') for route in route_elements]
    bus_routes_name = [route.text.strip() for route in route_elements]
    return bus_routes_link, bus_routes_name

def exportCsv(bus_details,fileName):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(bus_details)
    # Save the DataFrame to a CSV file
    df.to_csv(fileName, index=False)