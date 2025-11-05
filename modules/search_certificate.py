from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CERTIFICATES_URL
from modules.admin_login import admin_login

def search_certificate(driver):
    admin_login(driver)
    driver.get(CERTIFICATES_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter certificate's name to search: ")
    
    try:
        all_certificates = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        found = False
        for certificate in all_certificates:
            try:
                certificate_name = certificate.find_element(By.XPATH, ".//h3").text.strip()
                if certificate_name == search_name:
                    print(f"certificate '{certificate_name}' found.")
                    found = True
                    break
            except:
                continue
        
        if not found:
            print(f"certificate '{search_name}' not found.")
        
    except Exception as e:
        print(f"Error searching certificate: {e}")