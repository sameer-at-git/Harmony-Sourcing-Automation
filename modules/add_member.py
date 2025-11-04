from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import MEMBERS_URL
from modules.admin_login import admin_login

def add_member(driver):
    admin_login(driver)
    driver.get(MEMBERS_URL)


    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Member')]"))).click()
    name = input("Enter member name: ")
    position = input("Enter member position: ")
    description = input("Enter member description: ")
    image_path = input("Enter full path to image file (jpg/png/jpeg): ")
    order_number = input("Enter order number: ")
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]"))).send_keys(name)
    driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys(position)
    driver.find_element(By.CLASS_NAME, "ql-editor").send_keys(description)
    
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(image_path)
    
    
    driver.find_element(By.XPATH, "//input[@value='0']").send_keys(order_number)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    print(f"Member '{name}' added successfully.")