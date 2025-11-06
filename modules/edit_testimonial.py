from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.settings import TESTIMONIALS_URL
from modules.admin_login import admin_login

def edit_testimonial(driver):
    admin_login(driver)
    driver.get(TESTIMONIALS_URL)

    wait = WebDriverWait(driver, 10)
    search_name = input("Enter Testimonial name to edit: ").strip()

    try:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'grid')]/div")))
        all_testimonials = driver.find_elements(By.XPATH, "//div[contains(@class, 'grid')]/div")

        target_testimonial = None
        for testimonial in all_testimonials:
            try:
                name_element = testimonial.find_element(By.XPATH, ".//h3")
                if name_element.text.strip().lower() == search_name.lower():
                    target_testimonial = testimonial
                    break
            except:
                continue

        if not target_testimonial:
            print(f"Testimonial '{search_name}' not found.")
            return

        edit_button = target_testimonial.find_element(By.XPATH, ".//button[contains(@class, 'bg-blue-600')]")
        edit_button.click()

        name = input("Enter new name (leave blank to skip): ").strip()
        company = input("Enter new company (leave blank to skip): ").strip()
        description = input("Enter new description (leave blank to skip): ").strip()
        rating = input("Enter new rating (1-5, leave blank to skip): ").strip()
        order_number = input("Enter new order number (leave blank to skip): ").strip()
        image_path = input("Enter new image path (leave blank to skip): ").strip()

        if name:
            elem = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
            elem.clear()
            elem.send_keys(name)
        if company:
            elem = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
            elem.clear()
            elem.send_keys(company)
        if description:
            editor = driver.find_element(By.CLASS_NAME, "ql-editor")
            editor.clear()
            editor.send_keys(description)
        if rating:
            try:
                dropdown = Select(driver.find_element(By.XPATH, "//select[@class='w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent']"))
                rating_value = int(rating)
                if rating_value == 5:
                    dropdown.select_by_index(0)
                elif rating_value == 1:
                    dropdown.select_by_index(1)
                elif rating_value == 2:
                    dropdown.select_by_index(2)
                elif rating_value == 3:
                    dropdown.select_by_index(3)
                elif rating_value == 4:
                    dropdown.select_by_index(4)
            except:
                pass
        if order_number:
            order_elem = driver.find_element(By.XPATH, "//input[@value='0']")
            order_elem.clear()
            order_elem.send_keys(order_number)
        if image_path:
            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(image_path)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
        print(f"Testimonial '{search_name}' updated successfully.")
    except Exception as e:
        print(f"Error editing testimonial: {e}")
