from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import MEMBERS_URL
from modules.admin_login import admin_login

def delete_member(driver):
    admin_login(driver)
    driver.get(MEMBERS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter member name to delete: ")
    
    try:
        all_members = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        member_index = None
        for idx, member in enumerate(all_members, start=1):
            try:
                member_name = member.find_element(By.XPATH, ".//h3").text.strip()
                if member_name == search_name:
                    member_index = idx
                    break
            except:
                continue
        
        if member_index is None:
            print(f"Member '{search_name}' not found.")
            return
        
        if member_index == 1:
            delete_button_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']//div[1]//div[1]//div[2]//button[2]"
        else:
            delete_button_xpath = f"//div[{member_index}]//div[1]//div[2]//button[2]"
        
        driver.find_element(By.XPATH, delete_button_xpath).click()
        
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        
        wait.until(EC.staleness_of(all_members[member_index - 1]))
        
        verification_members = driver.find_elements(By.XPATH, f"//h3[normalize-space()='{search_name}']")
        
        if not verification_members:
            print(f"Member '{search_name}' deleted successfully.")
        else:
            print(f"Failed to delete member '{search_name}'.")
        
    except Exception as e:
        print(f"Error deleting member: {e}")