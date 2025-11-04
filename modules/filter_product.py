from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import PRODUCTS_URL
from modules.admin_login import admin_login

def filter_product(driver):
    admin_login(driver)
    driver.get(PRODUCTS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    print("\nFilter Products by status:")
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
        all_products = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        filtered_products = []
        for product in all_products:
            try:
                status_element = product.find_element(By.XPATH, f".{status_xpath}")
                product_name = product.find_element(By.XPATH, ".//h3").text.strip()
                filtered_products.append(product_name)
            except:
                continue
        
        if filtered_products:
            print(f"\n{status} Products:")
            for cat_name in filtered_products:
                print(f"- {cat_name}")
        else:
            print(f"{status} Products not found.")
        
    except Exception as e:
        print(f"Error filtering Products: {e}")