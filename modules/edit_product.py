from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config.settings import PRODUCTS_URL
from modules.admin_login import admin_login
import time

def edit_product(driver):
    admin_login(driver)
    driver.get(PRODUCTS_URL)

    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    product_name = input("Enter the product name to edit: ")

    products_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div"
    last_height = driver.execute_script("return document.body.scrollHeight")
    found = False

    while True:
        products = driver.find_elements(By.XPATH, products_xpath)
        for product in products:
            if product_name.lower() in product.text.lower():
                edit_button = product.find_element(By.XPATH, ".//button[contains(text(), 'Edit')]")
                driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)
                time.sleep(1)
                edit_button.click()
                found = True
                break
        if found:
            break
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    if not found:
        print("Product not found.")
        return

    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))

    name = input("Enter new Product name: ")
    description = input("Enter new product description: ")

    category_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@class='w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-purple-500']")))
    select = Select(category_dropdown)
    categories = [option.text for option in select.options if option.text.strip()]
    print("Available categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    choice = int(input("Select new category number: "))
    category_name = categories[choice - 1]

    image_path = input("Enter new full path to image file (jpg/png/jpeg): ")
    order_number = input("Enter new order number: ")

    name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
    name_field.clear()
    name_field.send_keys(name)
    driver.find_element(By.CLASS_NAME, "ql-editor").clear()
    driver.find_element(By.CLASS_NAME, "ql-editor").send_keys(description)
    select.select_by_visible_text(category_name)
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(image_path)
    order_field = driver.find_element(By.XPATH, "//input[@value='0']")
    order_field.clear()
    order_field.send_keys(order_number)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    print(f"Product '{name}' edited successfully.")
