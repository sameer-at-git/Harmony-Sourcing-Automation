from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CATEGORIES_URL
from modules.admin_login import admin_login

def delete_category(driver):
    admin_login(driver)
    driver.get(CATEGORIES_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter category name to delete: ")
    
    try:
        all_categories = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        category_index = None
        for idx, category in enumerate(all_categories, start=1):
            try:
                category_name = category.find_element(By.XPATH, ".//h3").text.strip()
                if category_name == search_name:
                    category_index = idx
                    break
            except:
                continue
        
        if category_index is None:
            print(f"Category '{search_name}' not found.")
            return
        
        if category_index == 1:
            delete_button_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']//div[1]//div[1]//div[2]//button[2]"
        else:
            delete_button_xpath = f"//div[{category_index}]//div[1]//div[2]//button[2]"
        
        driver.find_element(By.XPATH, delete_button_xpath).click()
        
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        
        wait.until(EC.staleness_of(all_categories[category_index - 1]))
        
        verification_categories = driver.find_elements(By.XPATH, f"//h3[normalize-space()='{search_name}']")
        
        if not verification_categories:
            print(f"Category '{search_name}' deleted successfully.")
        else:
            print(f"Failed to delete category '{search_name}'.")
        
    except Exception as e:
        print(f"Error deleting category: {e}")