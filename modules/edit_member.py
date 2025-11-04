from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import MEMBERS_URL
from modules.admin_login import admin_login

def edit_member(driver):
    admin_login(driver)
    driver.get(MEMBERS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter member name to edit: ")
    
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
            edit_button_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']//div[1]//div[1]//div[2]//button[1]"
        else:
            edit_button_xpath = f"//div[{member_index}]//div[1]//div[2]//button[1]"
        
        driver.find_element(By.XPATH, edit_button_xpath).click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
        
        name = input("Enter new member name: ")
        position = input("Enter new member position: ")
        description = input("Enter new member description: ")
        image_path = input("Enter full path to image file (leave blank to skip): ")
        order_number = input("Enter new order number: ")
        
        name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        name_field.clear()
        name_field.send_keys(name)
        
        position_field = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
        position_field.clear()
        position_field.send_keys(position)
        
        description_field = driver.find_element(By.CLASS_NAME, "ql-editor")
        description_field.clear()
        description_field.send_keys(description)
        
        if image_path:
            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(image_path)
        
        order_field = driver.find_element(By.XPATH, "//input[@value='0']")
        order_field.clear()
        order_field.send_keys(order_number)
        
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
        print(f"Member '{name}' updated successfully.")
        
    except Exception as e:
        print(f"Error editing member: {e}")