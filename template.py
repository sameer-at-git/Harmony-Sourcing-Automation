import os

def create_module_structure():
    modules = [
        'navigate_home',
        'navigate_products', 
        'navigate_categories',
        'navigate_client',
        'navigate_certificate',
        'navigate_contact',
        'navigate_testimonial',
        'navigate_user',
        'admin_login',
        'check_status',
        'add_member',
        'edit_member',
        'delete_member',
        'search_member',
        'add_category',
        'edit_category',
        'delete_category',
        'search_category',
        'filter_category',
        'add_product',
        'edit_product',
        'delete_product',
        'search_product',
        'filter_product',
        'add_client',
        'edit_client',
        'delete_client',
        'search_client',
        'filter_client',
        'add_certificate',
        'edit_certificate',
        'delete_certificate',
        'search_certificate',
        'filter_certificate',
        'add_contact',
        'edit_contact',
        'delete_contact',
        'search_contact',
        'filter_contact',
        'add_testimonial',
        'edit_testimonial',
        'delete_testimonial',
        'search_testimonial',
        'filter_testimonial',
        'add_user',
        'edit_user',
        'delete_user',
        'search_user',
        'filter_user'
    ]
    
    os.makedirs('modules', exist_ok=True)
    os.makedirs('config', exist_ok=True)
    os.makedirs('drivers', exist_ok=True)
    
    with open('modules/__init__.py', 'w') as f:
        pass
    
    with open('config/__init__.py', 'w') as f:
        pass
    
    for module in modules:
        filename = f"modules/{module}.py"
        with open(filename, 'w') as f:
            pass

if __name__ == "__main__":
    create_module_structure()