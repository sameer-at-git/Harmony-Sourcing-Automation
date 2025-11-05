from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.settings import PRODUCTS_URL
from modules.admin_login import admin_login

def add_product(driver):
    admin_login(driver)
    driver.get(PRODUCTS_URL)

    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Product')]"))).click()
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

    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]"))).send_keys(name)
    driver.find_element(By.CLASS_NAME, "ql-editor").send_keys(description)

    select.select_by_visible_text(product_name)

    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(image_path)
    driver.find_element(By.XPATH, "//input[@value='0']").send_keys(order_number)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    print(f"Product '{name}' added successfully.")
