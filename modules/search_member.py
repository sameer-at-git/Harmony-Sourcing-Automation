from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import MEMBERS_URL
from modules.admin_login import admin_login

def search_member(driver):
    admin_login(driver)
    driver.get(MEMBERS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter member name to search: ")
    
    try:
        all_members = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        found = False
        for member in all_members:
            try:
                member_name = member.find_element(By.XPATH, ".//h3").text.strip()
                if member_name == search_name:
                    position = member.find_element(By.XPATH, ".//p").text.strip()
                    print(f"\nMember found:")
                    print(f"Name: {member_name}")
                    print(f"Position: {position}")
                    found = True
                    break
            except:
                continue
        
        if not found:
            print(f"Member '{search_name}' not found.")
        
    except Exception as e:
        print(f"Error searching member: {e}")