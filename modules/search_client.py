from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CLIENTS_URL
from modules.admin_login import admin_login

def search_client(driver):
    admin_login(driver)
    driver.get(CLIENTS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter client's name to search: ")
    
    try:
        all_clients = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        found = False
        for client in all_clients:
            try:
                client_name = client.find_element(By.XPATH, ".//h3").text.strip()
                if client_name == search_name:
                    print(f"client '{client_name}' found.")
                    found = True
                    break
            except:
                continue
        
        if not found:
            print(f"client '{search_name}' not found.")
        
    except Exception as e:
        print(f"Error searching client: {e}")