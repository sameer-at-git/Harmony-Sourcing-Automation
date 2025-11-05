from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.settings import CLIENTS_URL
from modules.admin_login import admin_login
import time

def edit_client(driver):
    admin_login(driver)
    driver.get(CLIENTS_URL)
    wait = WebDriverWait(driver, 10)
    search_name = input("Enter client name to edit: ")
    grid_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div"
    found = False
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        items = driver.find_elements(By.XPATH, grid_xpath)
        for idx, item in enumerate(items, start=1):
            try:
                h3_xpath = f"({grid_xpath})[{idx}]//h3"
                name_el = driver.find_element(By.XPATH, h3_xpath)
                if name_el.text.strip().lower() == search_name.strip().lower():
                    edit_button_xpath = f"({grid_xpath})[{idx}]//div[1]//div[2]//button[1]"
                    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, edit_button_xpath))
                    time.sleep(0.5)
                    driver.find_element(By.XPATH, edit_button_xpath).click()
                    found = True
                    break
            except:
                continue
        if found:
            break
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    if not found:
        print(f"client '{search_name}' not found.")
        return
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    name = input("Enter client name: ")
    logo_path = input("Enter full path to logo file (jpg/png/jpeg): ")
    order_number = input("Enter order number: ")
    name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
    name_field.clear()
    name_field.send_keys(name)
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(logo_path)
    order_field = driver.find_element(By.XPATH, "//label[contains(text(), 'Order')]/following-sibling::input")
    order_field.clear()
    order_field.send_keys(order_number)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    print(f"client '{name}' edited successfully.")
