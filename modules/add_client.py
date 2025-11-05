from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CLIENTS_URL
from modules.admin_login import admin_login

def add_client(driver):
    admin_login(driver)
    driver.get(CLIENTS_URL)

    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Client')]"))).click()
    name = input("Enter client name: ")
    logo_path = input("Enter full path to logo file (jpg/png/jpeg): ")
    order_number = input("Enter order number: ")

    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]"))).send_keys(name)
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(logo_path)
    driver.find_element(By.XPATH, "//input[@value='0']").send_keys(order_number)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    print(f"client '{name}' added successfully.")
