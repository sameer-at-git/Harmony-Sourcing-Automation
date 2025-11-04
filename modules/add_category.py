from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.settings import CATEGORIES_URL
from modules.admin_login import admin_login
import emoji
import pyperclip

def add_category(driver):
    admin_login(driver)
    driver.get(CATEGORIES_URL)
    
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Category']"))).click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    
    print("\nCommon fashion emojis:")
    print(":dress: :jeans: :t-shirt: :womans_clothes: :mans_shoe:")
    print(":high_heel: :handbag: :necktie: :shirt: :running_shoe:")
    print(":baby: :child: :woman: :man: :sparkles:")
    
    name = input("\nEnter category name: ")
    description = input("Enter category description: ")
    emoji_input = input("Enter emoji shortcode (e.g., :dress:, :shirt:): ")
    emoji_char = emoji.emojize(emoji_input)
    order_number = input("Enter order number: ")
    
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys(name)
    driver.find_element(By.CLASS_NAME, "ql-editor").send_keys(description)
    
    emoji_field = driver.find_element(By.XPATH, "//input[@placeholder='🧶']")
    emoji_field.click()
    pyperclip.copy(emoji_char)
    emoji_field.send_keys(Keys.CONTROL, 'v')
    
    driver.find_element(By.XPATH, "//input[@value='0']").send_keys(order_number)
    
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
    print(f"Category '{name}' added successfully.")