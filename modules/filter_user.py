from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import USERS_URL
from modules.admin_login import admin_login

def filter_user(driver):
    admin_login(driver)
    driver.get(USERS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    print("\nFilter users by status:")
    print("1. Active")
    print("2. Inactive")
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        status = "Active"
        status_xpath = "//span[normalize-space()='Active']"
    elif choice == "2":
        status = "Inactive"
        status_xpath = "//span[normalize-space()='Inactive']"
    else:
        print("Invalid choice.")
        return
    
    try:
        all_users = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        filtered_users = []
        for user in all_users:
            try:
                user_status_element = user.find_element(By.XPATH, f".{status_xpath}")
                user_email = user.find_element(By.XPATH, ".//h3").text.strip()
                filtered_users.append(user_email)
            except:
                continue
        
        if filtered_users:
            print(f"\n{status} users:")
            for email in filtered_users:
                print(f"- {email}")
        else:
            print(f"No {status} users found.")
    
    except Exception as e:
        print(f"Error filtering users: {e}")
