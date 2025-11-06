from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.settings import TESTIMONIALS_URL
from modules.admin_login import admin_login

def add_testimonial(driver):
    admin_login(driver)
    driver.get(TESTIMONIALS_URL)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Testimonial')]"))).click()

    name = input("Enter name: ")
    company_name = input("Enter company name: ")
    description = input("Enter testimonial description: ")
    star_input = input("Enter star rating (1-5, optional, default 5): ")
    order_number = input("Enter order number (default 0): ") or "0"
    image_path = input("Enter full path to image file (optional): ")

    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]"))).send_keys(name)
    driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys(company_name)
    driver.find_element(By.CLASS_NAME, "ql-editor").send_keys(description)

    if star_input.strip():
        select = Select(driver.find_element(By.XPATH, "//select[@class='w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent']"))
        star_val = int(star_input)
        star_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        select.select_by_index(star_map.get(star_val, 0))

    order_input = driver.find_element(By.XPATH, "//input[@value='0']")
    order_input.clear()
    order_input.send_keys(order_number)

    if image_path.strip():
        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(image_path)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    print(f"testimonial '{name}' added successfully.")
