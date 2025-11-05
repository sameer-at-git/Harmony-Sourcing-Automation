from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CLIENTS_URL
from modules.admin_login import admin_login

def filter_client(driver):
    admin_login(driver)
    driver.get(CLIENTS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    print("\nFilter clients by status:")
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
        all_clients = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        filtered_clients = []
        for client in all_clients:
            try:
                status_element = client.find_element(By.XPATH, f".{status_xpath}")
                client_name = client.find_element(By.XPATH, ".//h3").text.strip()
                filtered_clients.append(client_name)
            except:
                continue
        
        if filtered_clients:
            print(f"\n{status} clients:")
            for cat_name in filtered_clients:
                print(f"- {cat_name}")
        else:
            print(f"{status} clients not found.")
        
    except Exception as e:
        print(f"Error filtering clients: {e}")