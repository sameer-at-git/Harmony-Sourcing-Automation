from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import USERS_URL
from modules.admin_login import admin_login

def edit_user(driver):
    admin_login(driver)
    driver.get(USERS_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter user's name to edit: ").strip()
    try:
        all_users = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        user_index = None
        for idx, user in enumerate(all_users, start=1):
            try:
                user_name = user.find_element(By.XPATH, ".//h3").text.strip()
                if user_name == search_name:
                    user_index = idx
                    break
            except:
                continue
        
        if user_index is None:
            print(f"User '{search_name}' not found.")
            return
        
        edit_button = all_users[user_index - 1].find_element(By.XPATH, ".//button[contains(@class,'text-blue-400')]")
        edit_button.click()
        
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        current_email = email_input.get_attribute("value")
        email = input(f"Enter new email (leave blank to keep '{current_email}'): ").strip()
        if email and not email.isspace():
            email_input.clear()
            email_input.send_keys(email)
        else:
            email = current_email
        
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password = input("Enter new password (leave blank to keep current): ").strip()
        if password and not password.isspace():
            password_input.clear()
            password_input.send_keys(password)
        
        role_select = driver.find_element(By.XPATH, "//select")
        role = input("Enter role (admin/super_admin, leave blank to keep current): ").strip()
        if role:
            for option in role_select.find_elements(By.TAG_NAME, "option"):
                if option.get_attribute("value") == role:
                    option.click()
                    break
        
        checkbox = driver.find_element(By.ID, "editReceiveEmail")
        receive_email_input = input("Receive email notifications? (y/n, leave blank to keep current): ").strip().lower()
        if receive_email_input == 'y' and not checkbox.is_selected():
            checkbox.click()
        elif receive_email_input == 'n' and checkbox.is_selected():
            checkbox.click()
        
        update_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(),'Update User')]")
        update_button.click()
        
        wait.until(EC.presence_of_element_located((By.XPATH, f"//h3[normalize-space()='{email}']")))
        print(f"User '{search_name}' updated successfully.")
    
    except Exception as e:
        print(f"Error editing user: {e}")
