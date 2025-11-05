from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.settings import PRODUCTS_URL
from modules.admin_login import admin_login
import time

def edit_product(driver):
    admin_login(driver)
    driver.get(PRODUCTS_URL)
    wait = WebDriverWait(driver, 10)
    search_name = input("Enter product name to edit: ")
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
        print(f"Product '{search_name}' not found.")
        return
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    name = input("Enter Product name: ")
    description = input("Enter product description: ")
    product_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@class='w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-purple-500']")))
    select = Select(product_dropdown)
    products = [option.text for option in select.options if option.text.strip()]
    print("Available products:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product}")
    choice = int(input("Select product number: "))
    product_name = products[choice - 1]
    image_path = input("Enter full path to image file (jpg/png/jpeg): ")
    order_number = input("Enter order number: ")
    name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
    name_field.clear()
    name_field.send_keys(name)
    description_field = driver.find_element(By.CLASS_NAME, "ql-editor")
    description_field.clear()
    description_field.send_keys(description)
    select.select_by_visible_text(product_name)
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(image_path)
    order_field = driver.find_element(By.XPATH, "//label[contains(text(), 'Order')]/following-sibling::input")
    order_field.clear()
    order_field.send_keys(order_number)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    print(f"Product '{name}' edited successfully.")
