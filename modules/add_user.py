from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import USERS_URL
from modules.admin_login import admin_login

def add_user(driver):
    admin_login(driver)
    driver.get(USERS_URL)

    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add User')]"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//form")))

    email = input("Enter user email: ").strip()
    password = input("Enter user password: ").strip()
    role = input("Enter role (admin/super_admin): ").strip()
    receive_email = input("Receive email notifications? (y/n): ").strip().lower() == 'y'

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[text()='Password']/following-sibling::input").send_keys(password)
    role_select = driver.find_element(By.XPATH, "//label[text()='Role']/following-sibling::select")
    role_select.send_keys(role)

    if receive_email:
        checkbox = driver.find_element(By.ID, "receiveEmail")
        if not checkbox.is_selected():
            checkbox.click()

    driver.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Add User')]").click()

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, f"//h3[text()='{email}']")))
        print(f"User '{email}' added successfully.")
    except:
        print(f"Failed to add user '{email}'.")
