from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CATEGORIES_URL
from modules.admin_login import admin_login

def search_category(driver):
    admin_login(driver)
    driver.get(CATEGORIES_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter category name to search: ")
    
    try:
        all_categories = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        found = False
        for category in all_categories:
            try:
                category_name = category.find_element(By.XPATH, ".//h3").text.strip()
                if category_name == search_name:
                    print(f"\nCategory '{category_name}' found.")
                    found = True
                    break
            except:
                continue
        
        if not found:
            print(f"Category '{search_name}' not found.")
        
    except Exception as e:
        print(f"Error searching category: {e}")