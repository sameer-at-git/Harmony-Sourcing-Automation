from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.settings import BASE_URL
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service("./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url= BASE_URL
    driver.get(url)
    return driver

def close_driver(driver):
    driver.quit()

def show_menu():
    print("\n1. Navigate Home")
    print("2. Navigate Home/Products")
    print("3. Admin Login")
    print("----------------------------------")    
    print("4. Add Member")
    print("5. Edit Member")
    print("6. Delete Member")
    print("7. Search Member")
    print("----------------------------------")
    print("8. Navigate Categories")
    print("9. Add Category")
    print("10. Edit Category")
    print("11. Delete Category")
    print("12. Search Category")
    print("13. Filter Category")
    print("----------------------------------")
    print("14. Navigate Products")
    print("15. Add Product")
    print("16. Edit Product")
    print("17. Delete Product")
    print("18. Search Product")
    print("19. Filter Product")
    print("----------------------------------")
    print("20. Navigate Clients")    
    print("21. Add Client")
    print("22. Edit Client")
    print("23. Delete Client")
    print("24. Search Client")
    print("25. Filter Client")
    print("----------------------------------")
    print("26. Navigate Certificate")    
    print("27. Add Certificate")
    print("28. Edit Certificate")
    print("29. Delete Certificate")
    print("30. Search Certificate")
    print("31. Filter Certificate")
    print("----------------------------------")
    print("32. Navigate Contacts")      
    print("33. Add Contact")
    print("34. Edit Contact")
    print("35. Delete Contact")
    print("36. Search Contact")
    print("37. Filter Contact")
    print("----------------------------------")
    print("38. Navigate Testimonials")    
    print("39. Add Testimonial")
    print("40. Edit Testimonial")
    print("41. Delete Testimonial")
    print("42. Search Testimonial")
    print("43. Filter Testimonial")
    print("----------------------------------")
    print("44. Navigate Users")     
    print("45. Add User")
    print("46. Edit User")
    print("47. Delete User")
    print("48. Search User")
    print("49. Filter User")
    print("----------------------------------")
    print("50. Exit")

def main():
    
    
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        driver = setup_driver()
        if choice == '1':
            from modules.navigate_home import navigate_home
            navigate_home(driver)
            close_driver(driver)
        elif choice == '2':
            from modules.navigate_home_products import navigate_home_products
            navigate_home_products(driver)
            close_driver(driver)
        elif choice == '3':
            from modules.admin_login import admin_login
            admin_login(driver)
            close_driver(driver)
        elif choice == '4':
            from modules.add_member import add_member
            add_member(driver) 
            close_driver(driver)
        elif choice == '5':
            from modules.edit_member import edit_member
            edit_member(driver) 
            close_driver(driver)
        elif choice == '6':
            from modules.delete_member import delete_member
            delete_member(driver) 
            close_driver(driver)
        elif choice == '7':
            from modules.search_member import search_member
            search_member(driver) 
            close_driver(driver)
        elif choice == '8':
            from modules.navigate_categories import navigate_categories
            navigate_categories(driver) 
            close_driver(driver)
        elif choice == '9':
            from modules.add_category import add_category
            add_category(driver)
            close_driver(driver)
        elif choice == '10':
            from modules.edit_category import edit_category
            edit_category(driver) 
            close_driver(driver)
        elif choice == '11':
            from modules.delete_category import delete_category
            delete_category(driver) 
            close_driver(driver)
        elif choice == '12':
            from modules.search_category import search_category
            search_category(driver) 
            close_driver(driver)
        elif choice == '13':
            from modules.filter_category import filter_category
            filter_category(driver)  
            close_driver(driver)
        elif choice == '14':
            from modules.navigate_home_products import navigate_product
            navigate_product(driver) 
            close_driver(driver)
        elif choice == '15':
            from modules.add_product import add_product
            add_product(driver) 
            close_driver(driver)
        elif choice == '16':
            from modules.edit_product import edit_product
            edit_product(driver) 
            close_driver(driver)
        elif choice == '17':
            from modules.delete_product import delete_product
            delete_product(driver) 
            close_driver(driver)
        elif choice == '18':
            from modules.search_product import search_product
            search_product(driver) 
            close_driver(driver)
        elif choice == '19':
            from modules.filter_product import filter_product
            filter_product(driver)  
            close_driver(driver)    
        elif choice == '20':
            from modules.navigate_client import navigate_client
            navigate_client(driver) 
            close_driver(driver)
        elif choice == '21':
            from modules.add_client import add_client
            add_client(driver) 
            close_driver(driver)
        elif choice == '22':
            from modules.edit_client import edit_client
            edit_client(driver) 
            close_driver(driver)
        elif choice == '23':
            from modules.delete_client import delete_client
            delete_client(driver) 
            close_driver(driver)
        elif choice == '24':
            from modules.search_client import search_client
            search_client(driver) 
            close_driver(driver)
        elif choice == '25':
            from modules.filter_client import filter_client
            filter_client(driver) 
            close_driver(driver)
        elif choice == '26':
            from modules.navigate_certificate import navigate_certificate
            navigate_certificate(driver) 
            close_driver(driver)
        elif choice == '27':
            from modules.add_certificate import add_certificate
            add_certificate(driver) 
            close_driver(driver)
        elif choice == '28':
            from modules.edit_certificate import edit_certificate
            edit_certificate(driver) 
            close_driver(driver)
        elif choice == '29':
            from modules.delete_certificate import delete_certificate
            delete_certificate(driver) 
            close_driver(driver)
        elif choice == '30':
            from modules.search_certificate import search_certificate
            search_certificate(driver) 
            close_driver(driver)
        elif choice == '31':
            from modules.filter_certificate import filter_certificate
            filter_certificate(driver) 
            close_driver(driver)  
        elif choice == '32':
            from modules.navigate_certificate import navigate_certificate
            navigate_certificate(driver) 
            close_driver(driver)
        elif choice == '33':
            from modules.add_certificate import add_certificate
            add_certificate(driver) 
            close_driver(driver)
        elif choice == '34':
            from modules.edit_certificate import edit_certificate
            edit_certificate(driver) 
            close_driver(driver)
        elif choice == '35':
            from modules.delete_certificate import delete_certificate
            delete_certificate(driver) 
            close_driver(driver)
        elif choice == '36':
            from modules.search_certificate import search_certificate
            search_certificate(driver) 
            close_driver(driver)
        elif choice == '37':
            from modules.filter_certificate import filter_certificate
            filter_certificate(driver)  
            close_driver(driver)    
        elif choice == '38':
            from modules.navigate_testimonial import navigate_testimonial
            navigate_testimonial(driver) 
            close_driver(driver)
        elif choice == '39':
            from modules.add_testimonial  import add_testimonial
            add_testimonial(driver) 
            close_driver(driver)
        elif choice == '40':
            from modules.edit_testimonial  import edit_testimonial
            edit_testimonial(driver) 
            close_driver(driver)
        elif choice == '41':
            from modules.delete_testimonial  import delete_testimonial
            delete_testimonial(driver) 
            close_driver(driver)
        elif choice == '42':
            from modules.search_testimonial  import search_testimonial
            search_testimonial(driver) 
            close_driver(driver)
        elif choice == '43':
            from modules.filter_testimonial import filter_testimonial
            filter_testimonial(driver) 
            close_driver(driver) 
        elif choice == '44':
            from modules.navigate_user import filter_testimonial
            filter_testimonial(driver) 
            close_driver(driver)
        elif choice == '45':
            from modules.add_user  import add_user
            add_user(driver) 
            close_driver(driver)
        elif choice == '46':
            from modules.edit_user  import edit_user
            edit_user(driver) 
            close_driver(driver)
        elif choice == '47':
            from modules.delete_user import delete_user
            delete_user(driver) 
            close_driver(driver)
        elif choice == '48':
            from modules.search_user  import search_user
            search_user(driver) 
            close_driver(driver)
        elif choice == '49':
            from modules.filter_user import filter_user
            filter_user(driver)  
            close_driver(driver)
                                                                                                                                                            
        elif choice == '50':
            break
        else:
            print("Function not implemented yet")
    
    close_driver(driver)

if __name__ == "__main__":
    main()