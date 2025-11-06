from selenium.webdriver.common.by import By
from config.settings import CONTACTS_URL
from modules.admin_login import admin_login
import time

def filter_contact(driver):
    admin_login(driver)
    driver.get(CONTACTS_URL)
    time.sleep(2)

    print("\nFilter contacts by status:")
    print("1. New")
    print("2. Read")
    print("3. Replied")
    print("4. Closed")
    choice = input("Enter choice (1-4): ")

    color_map = {
        "1": "bg-blue-500",
        "2": "bg-yellow-500",
        "3": "bg-green-500",
        "4": "bg-gray-500"
    }

    status_map = {
        "1": "New",
        "2": "Read",
        "3": "Replied",
        "4": "Closed"
    }

    if choice not in color_map:
        print("Invalid choice.")
        return

    color_class = color_map[choice]
    status = status_map[choice]

    try:
        contacts = driver.find_elements(By.XPATH, f"//tr[.//select[contains(@class,'{color_class}')]]")
        names = []

        for contact in contacts:
            try:
                name = contact.find_element(By.XPATH, ".//div[@class='text-sm font-medium text-white']").text.strip()
                names.append(name)
            except:
                continue

        if names:
            print(f"\n{status} contacts:")
            for n in names:
                print(f"- {n}")
        else:
            print(f"No {status} contacts found.")
    except Exception as e:
        print(f"Error filtering contacts: {e}")
