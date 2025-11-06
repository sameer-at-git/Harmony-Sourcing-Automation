from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import TESTIMONIALS_URL
from modules.admin_login import admin_login

def delete_testimonial(driver):
    admin_login(driver)
    driver.get(TESTIMONIALS_URL)
    
    wait = WebDriverWait(driver, 10)
    search_name = input("Enter Testimonial name to delete: ").strip()

    try:
        wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'grid')]/div")
        ))
        all_testimonials = driver.find_elements(By.XPATH, "//div[contains(@class, 'grid')]/div")

        found = False
        for testimonial in all_testimonials:
            try:
                name_element = testimonial.find_element(By.XPATH, ".//h3")
                name_text = name_element.text.strip()

                if name_text.lower() == search_name.lower():
                    delete_button = testimonial.find_element(
                        By.XPATH, ".//button[contains(@class, 'bg-red-600')]"
                    )
                    delete_button.click()
                    found = True
                    break
            except Exception:
                continue

        if not found:
            print(f"Testimonial '{search_name}' not found.")
            return

        # Wait for confirmation alert
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        # Wait for testimonial to be removed from DOM
        wait.until(EC.staleness_of(testimonial))

        # Re-check page for confirmation
        still_exists = driver.find_elements(
            By.XPATH, f"//h3[normalize-space()='{search_name}']"
        )
        if not still_exists:
            print(f"Testimonial '{search_name}' deleted successfully.")
        else:
            print(f"Failed to delete testimonial '{search_name}'.")
            
    except Exception as e:
        print(f"Error deleting testimonial: {e}")
