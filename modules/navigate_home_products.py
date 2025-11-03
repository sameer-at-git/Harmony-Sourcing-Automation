from selenium.webdriver.common.by import By
from config.settings import BASE_URL
import time

def navigate_home_products(driver):
    driver.get(BASE_URL)
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class='harmony-nav-link' and @href='/products']").click()
    time.sleep(2)
    print("Navigated to Products Page Successfully.")
