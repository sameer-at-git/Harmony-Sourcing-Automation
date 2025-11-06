from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import TESTIMONIALS_URL
from modules.admin_login import admin_login

def search_testimonial(driver):
    admin_login(driver)
    driver.get(TESTIMONIALS_URL)

    search_name = input("Enter Testimonial name to search: ").strip()
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'grid')]/div")))
        all_testimonials = driver.find_elements(By.XPATH, "//div[contains(@class, 'grid')]/div")

        for testimonial in all_testimonials:
            try:
                name_element = testimonial.find_element(By.XPATH, ".//h3")
                if name_element.text.strip().lower() == search_name.lower():
                    print(f"Testimonial '{search_name}' found.")
                    return
            except:
                continue

        print(f"Testimonial '{search_name}' not found.")
    except Exception as e:
        print(f"Error searching testimonial: {e}")
