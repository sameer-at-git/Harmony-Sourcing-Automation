from selenium.webdriver.common.by import By
from config.settings import BASE_URL
import time

def navigate_home(driver):
    driver.get(BASE_URL)
    time.sleep(2)
    print("Navigated to Home Page Successfully.")
