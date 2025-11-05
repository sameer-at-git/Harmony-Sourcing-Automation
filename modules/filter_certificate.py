from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import CERTIFICATES_URL
from modules.admin_login import admin_login

def filter_certificate(driver):
    admin_login(driver)
    driver.get(CERTIFICATES_URL)
    
    wait = WebDriverWait(driver, 10)
    
    print("\nFilter certificates by status:")
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
        all_certificates = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        filtered_certificates = []
        for certificate in all_certificates:
            try:
                status_element = certificate.find_element(By.XPATH, f".{status_xpath}")
                certificate_name = certificate.find_element(By.XPATH, ".//h3").text.strip()
                filtered_certificates.append(certificate_name)
            except:
                continue
        
        if filtered_certificates:
            print(f"\n{status} certificates:")
            for cat_name in filtered_certificates:
                print(f"- {cat_name}")
        else:
            print(f"{status} certificates not found.")
        
    except Exception as e:
        print(f"Error filtering certificates: {e}")