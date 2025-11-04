from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import PRODUCTS_URL
from modules.admin_login import admin_login

def delete_product(driver):
    admin_login(driver)
    driver.get(PRODUCTS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter product name to delete: ")
    
    try:
        all_product = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        product_index = None
        for idx, product in enumerate(all_product, start=1):
            try:
                product_name = product.find_element(By.XPATH, ".//h3").text.strip()
                if product_name == search_name:
                    product_index = idx
                    break
            except:
                continue
        
        if product_index is None:
            print(f"Category '{search_name}' not found.")
            return
        
        if product_index == 1:
            delete_button_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']//div[1]//div[1]//div[2]//button[2]"
        else:
            delete_button_xpath = f"//div[{product_index}]//div[1]//div[2]//button[2]"
        
        driver.find_element(By.XPATH, delete_button_xpath).click()
        
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        
        wait.until(EC.staleness_of(all_product[product_index - 1]))
        
        verification_product = driver.find_elements(By.XPATH, f"//h3[normalize-space()='{search_name}']")
        
        if not verification_product:
            print(f"Product '{search_name}' deleted successfully.")
        else:
            print(f"Failed to delete category '{search_name}'.")
        
    except Exception as e:
        print(f"Error deleting category: {e}")