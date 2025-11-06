from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import USERS_URL
from modules.admin_login import admin_login

def delete_user(driver):
    admin_login(driver)
    driver.get(USERS_URL)

    wait = WebDriverWait(driver, 10)

    search_name = input("Enter user email to delete: ").strip()

    try:
        all_users = driver.find_elements(By.XPATH, "//div[contains(@class,'grid')]//div")
        user_index = None
        for idx, user in enumerate(all_users, start=1):
            try:
                user_email = user.find_element(By.XPATH, ".//h3").text.strip()
                if user_email == search_name:
                    user_index = idx
                    break
            except:
                continue

        if user_index is None:
            print(f"User '{search_name}' not found.")
            return

        delete_button = driver.find_element(By.XPATH, f"(//div[contains(@class,'grid')]//div)[{user_index}]//button[contains(@class,'text-red-400')]")
        delete_button.click()

        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        wait.until(EC.staleness_of(all_users[user_index - 1]))

        remaining = driver.find_elements(By.XPATH, f"//h3[text()='{search_name}']")
        if not remaining:
            print(f"User '{search_name}' deleted successfully.")
        else:
            print(f"Failed to delete user '{search_name}'.")

    except Exception as e:
        print(f"Error deleting user: {e}")
