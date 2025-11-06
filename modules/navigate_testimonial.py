from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import TESTIMONIALS_URL
from modules.admin_login import admin_login
import time


def navigate_testimonial(driver):
    admin_login(driver)
    driver.get(TESTIMONIALS_URL)
    time.sleep(2)

    print("Navigated to testimonials Successfully")