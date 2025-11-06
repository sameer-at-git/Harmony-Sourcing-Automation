from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import USERS_URL
from modules.admin_login import admin_login

def search_user(driver):
    admin_login(driver)
    driver.get(USERS_URL)

    wait = WebDriverWait(driver, 10)
    search_name = input("Enter user email to search: ").strip()

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, f"//h3[text()='{search_name}']")))
        print(f"User '{search_name}' found.")
    except:
        print(f"User '{search_name}' not found.")
