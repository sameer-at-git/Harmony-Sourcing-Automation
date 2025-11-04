from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from config.settings import MEMBERS_URL
from modules.admin_login import admin_login
import time

def edit_member(driver):
    admin_login(driver)
    driver.get(MEMBERS_URL)
    time.sleep(2)

    member_name = input("Enter the name of the member to edit: ")

    edit_button = driver.find_element(By.XPATH, f"//tr[contains(., '{member_name}')]//a[contains(., 'Edit')]")
    edit_button.click()
    
    time.sleep(2)

    new_name = input("Enter new member name (or press Enter to skip): ")
    if new_name:
        name_input = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
        name_input.clear()
        name_input.send_keys(new_name)

    new_position = input("Enter new member position (or press Enter to skip): ")
    if new_position:
        position_input = driver.find_element(By.XPATH, "//input[@placeholder='Position']")
        position_input.clear()
        position_input.send_keys(new_position)

    new_description = input("Enter new member description (or press Enter to skip): ")
    if new_description:
        description_input = driver.find_element(By.CLASS_NAME, "ql-editor")
        description_input.clear()
        description_input.send_keys(new_description)

    new_image_path = input("Enter new full path to image file (or press Enter to skip): ")
    if new_image_path:
        image_input = driver.find_element(By.XPATH, "//input[@type='file']")
        image_input.send_keys(new_image_path)

    new_order_number = input("Enter new order number (or press Enter to skip): ")
    if new_order_number:
        order_input = driver.find_element(By.XPATH, "//input[@placeholder='Order']")
        order_input.clear()
        order_input.send_keys(new_order_number)

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    
    time.sleep(2)

    print(f"Member '{member_name}' updated successfully.")

