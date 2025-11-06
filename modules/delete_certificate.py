from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CERTIFICATES_URL
from modules.admin_login import admin_login

def delete_certificate(driver):
    admin_login(driver)
    driver.get(CERTIFICATES_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter Certificate's name to delete: ")
    
    try:
        all_certificate = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        certificate_index = None
        for idx, certificate in enumerate(all_certificate, start=1):
            try:
                certificate_name = certificate.find_element(By.XPATH, ".//h3").text.strip()
                if certificate_name == search_name:
                    certificate_index = idx
                    break
            except:
                continue
        
        if certificate_index is None:
            print(f"certificate '{search_name}' not found.")
            return
        
        if certificate_index == 1:
            delete_button_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']//div[1]//div[1]//div[2]//button[2]"
        else:
            delete_button_xpath = f"//div[{certificate_index}]//div[1]//div[2]//button[2]"
        
        driver.find_element(By.XPATH, delete_button_xpath).click()
        
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        
        wait.until(EC.staleness_of(all_certificate[certificate_index - 1]))
        
        verification_certificate = driver.find_elements(By.XPATH, f"//h3[normalize-space()='{search_name}']")
        
        if not verification_certificate:
            print(f"certificate '{search_name}' deleted successfully.")
        else:
            print(f"Failed to delete certificate '{search_name}'.")
        
    except Exception as e:
        print(f"Error deleting certificate: {e}")