from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config.settings import CONTACTS_URL
from modules.admin_login import admin_login
import time

def edit_contact(driver):
    admin_login(driver)
    driver.get(CONTACTS_URL)
    time.sleep(2)

    contact_name = input("Enter contact name to edit: ")
    print("\nChange status to:")
    print("1. New")
    print("2. Read")
    print("3. Replied")
    print("4. Closed")
    choice = input("Enter choice (1-4): ")

    status_value_map = {
        "1": "new",
        "2": "read",
        "3": "replied",
        "4": "closed"
    }

    if choice not in status_value_map:
        print("Invalid choice.")
        return

    try:
        contact_row = driver.find_element(By.XPATH, f"//tr[.//div[normalize-space()='{contact_name}']]")
        dropdown = contact_row.find_element(By.XPATH, ".//select[contains(@class,'rounded-full')]")
        select = Select(dropdown)
        select.select_by_value(status_value_map[choice])
        time.sleep(1)
        print(f"Status for contact '{contact_name}' updated to '{status_value_map[choice].capitalize()}'.")
    except Exception as e:
        print(f"Error editing contact: {e}")
