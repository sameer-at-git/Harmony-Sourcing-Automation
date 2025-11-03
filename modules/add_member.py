from selenium.webdriver.common.by import By
from config.settings import MEMBERS_URL
from modules.admin_login import admin_login
import time

def add_member(driver):
    admin_login(driver)
    driver.get(MEMBERS_URL)
    name = input("Enter member name: ")
    position = input("Enter member position: ")
    description = input("Enter member description: ")
    image_path = input("Enter full path to image file (jpg/png/jpeg): ")
    order_number = input("Enter order number: ")

    
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add First Member']").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(name)
    driver.find_element(By.XPATH, "//input[@placeholder='Position']").send_keys(position)
    driver.find_element(By.CLASS_NAME, "ql-editor").send_keys(description)

    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(image_path)

    num_field = driver.find_element(By.XPATH, "//input[@value='0']")
    num_field.clear()
    num_field.send_keys(order_number)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    print(f"Member '{name}' added successfully.")
