from selenium.webdriver.common.by import By
from config.settings import LOGIN_URL,ADMIN_EMAIL,ADMIN_PASSWORD
import time

def admin_login(driver):
    driver.get(LOGIN_URL)
    time.sleep(2)

    driver.find_element(By.ID, "email").send_keys(ADMIN_EMAIL)
    driver.find_element(By.ID, "password").send_keys(ADMIN_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    try:
        error = driver.find_element(By.XPATH, "//div[@class='bg-red-50 text-red-600 p-3 rounded-lg text-sm']")
        if error.is_displayed():
            print("Invalid credentials.")
            return False
    except:
        print("Logged in Successfully.")
        return True
