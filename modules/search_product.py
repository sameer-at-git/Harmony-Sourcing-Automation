from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import PRODUCTS_URL
from modules.admin_login import admin_login

def search_product(driver):
    admin_login(driver)
    driver.get(PRODUCTS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter product name to search: ")
    
    try:
        all_products = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        found = False
        for product in all_products:
            try:
                product_name = product.find_element(By.XPATH, ".//h3").text.strip()
                if product_name == search_name:
                    print(f"\Product '{product_name}' found.")
                    found = True
                    break
            except:
                continue
        
        if not found:
            print(f"Product '{search_name}' not found.")
        
    except Exception as e:
        print(f"Error searching category: {e}")