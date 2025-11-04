from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.settings import CATEGORIES_URL
from modules.admin_login import admin_login
import emoji
import pyperclip

def edit_category(driver):
    admin_login(driver)
    driver.get(CATEGORIES_URL)
    
    wait = WebDriverWait(driver, 10)
    
    search_name = input("Enter category name to edit: ")
    
    try:
        all_categories = driver.find_elements(By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']/div")
        
        category_index = None
        for idx, category in enumerate(all_categories, start=1):
            try:
                category_name = category.find_element(By.XPATH, ".//h3").text.strip()
                if category_name == search_name:
                    category_index = idx
                    break
            except:
                continue
        
        if category_index is None:
            print(f"Category '{search_name}' not found.")
            return
        
        if category_index == 1:
            edit_button_xpath = "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']//div[1]//div[1]//div[2]//button[1]"
        else:
            edit_button_xpath = f"//div[{category_index}]//div[1]//div[2]//button[1]"
        
        driver.find_element(By.XPATH, edit_button_xpath).click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
        
        print("\nCommon fashion emojis:")
        print(":dress: :jeans: :t-shirt: :womans_clothes: :mans_shoe:")
        print(":high_heel: :handbag: :necktie: :shirt: :running_shoe:")
        print(":baby: :child: :woman: :man: :sparkles:")
        
        name = input("\nEnter new category name: ")
        description = input("Enter new category description: ")
        emoji_input = input("Enter emoji shortcode (e.g., :dress:, :shirt:): ")
        emoji_char = emoji.emojize(emoji_input)
        order_number = input("Enter new order number: ")
        
        name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        name_field.clear()
        name_field.send_keys(name)
        
        description_field = driver.find_element(By.CLASS_NAME, "ql-editor")
        description_field.clear()
        description_field.send_keys(description)
        
        emoji_field = driver.find_element(By.XPATH, "//input[@placeholder='🧶']")
        emoji_field.click()
        emoji_field.clear()
        pyperclip.copy(emoji_char)
        emoji_field.send_keys(Keys.CONTROL, 'v')
        
        order_field = driver.find_element(By.XPATH, "//input[@value='0']")
        order_field.clear()
        order_field.send_keys(order_number)
        
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
        print(f"Category '{name}' updated successfully.")
        
    except Exception as e:
        print(f"Error editing category: {e}")