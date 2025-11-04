from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CATEGORIES_URL
from modules.admin_login import admin_login

def filter_category(driver):
    admin_login(driver)
    driver.get(CATEGORIES_URL)
    
    wait = WebDriverWait(driver, 10)
    
    print("\nFilter categories by status:")
    print("1. Active")
    print("2. Inactive")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        status = "Active"
        status_xpath = "//span[@class='flex items-center text-green-400'][normalize-space()='Active']"
    elif choice == "2":
        status = "Inactive"
        status_xpath = "//span[@class='flex items-center text-red-400'][normalize-space()='Inactive']"
    else:
        print("Invalid choice.")
        return
    
    try:
        all_categories = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        filtered_categories = []
        for category in all_categories:
            try:
                status_element = category.find_element(By.XPATH, f".{status_xpath}")
                category_name = category.find_element(By.XPATH, ".//h3").text.strip()
                filtered_categories.append(category_name)
            except:
                continue
        
        if filtered_categories:
            print(f"\n{status} categories:")
            for cat_name in filtered_categories:
                print(f"- {cat_name}")
        else:
            print(f"{status} categories not found.")
        
    except Exception as e:
        print(f"Error filtering categories: {e}")