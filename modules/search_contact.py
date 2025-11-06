from selenium.webdriver.common.by import By
from config.settings import CONTACTS_URL
from modules.admin_login import admin_login
import time

def search_contact(driver):
    admin_login(driver)
    driver.get(CONTACTS_URL)
    time.sleep(2)

    name = input("Enter contact name to search: ").strip()
    elements = driver.find_elements(By.XPATH, f"//div[normalize-space()='{name}']")

    if elements:
        print(f"Contact '{name}' found.")
    else:
        print(f"Contact '{name}' not found.")
