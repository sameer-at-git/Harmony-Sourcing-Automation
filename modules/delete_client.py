from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CLIENTS_URL
from modules.admin_login import admin_login

def delete_client(driver):
    admin_login(driver)
    driver.get(CLIENTS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter Client's name to delete: ")
    
    try:
        all_client = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        client_index = None
        for idx, client in enumerate(all_client, start=1):
            try:
                client_name = client.find_element(By.XPATH, ".//h3").text.strip()
                if client_name == search_name:
                    client_index = idx
                    break
            except:
                continue
        
        if client_index is None:
            print(f"Client '{search_name}' not found.")
            return
        
        if client_index == 1:
            delete_button_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']//div[1]//div[1]//div[2]//button[2]"
        else:
            delete_button_xpath = f"//div[{client_index}]//div[1]//div[2]//button[2]"
        
        driver.find_element(By.XPATH, delete_button_xpath).click()
        
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        
        wait.until(EC.staleness_of(all_client[client_index - 1]))
        
        verification_client = driver.find_elements(By.XPATH, f"//h3[normalize-space()='{search_name}']")
        
        if not verification_client:
            print(f"client '{search_name}' deleted successfully.")
        else:
            print(f"Failed to delete client '{search_name}'.")
        
    except Exception as e:
        print(f"Error deleting client: {e}")