
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CONTACTS_URL
from modules.admin_login import admin_login
import time


def navigate_contact(driver):
    admin_login(driver)
    driver.get(CONTACTS_URL)
    time.sleep(2)

    print("Navigated to Contact Successfully")