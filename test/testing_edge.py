from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading
class SauceDemoTest:
    def __init__(self):
        self.driver = webdriver.Edge()
    
    
    def performance_testing(self, num_users=15):
        def user_simulation():
            driver = webdriver.Edge()
            driver.get("https://www.saucedemo.com/")
            time.sleep(1)
            username_field = driver.find_element(By.ID, "user-name")
            password_field = driver.find_element(By.ID, "password")
            login_button = driver.find_element(By.ID, "login-button")
            username_field.send_keys("standard_user")
            password_field.send_keys("secret_sauce")
            login_button.click()
            time.sleep(2)
            driver.quit()
        
        threads = []
        for _ in range(num_users):
            thread = threading.Thread(target=user_simulation)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        print(f"Performance test completed with {num_users} users logging in simultaneously.")
        
            
    def boundary_login_testing(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        time.sleep(2)
        
        test_values = ["", "a", "standard_user_standard_user_standard_user_standard_user", "123456789012345678901234567890"]
        
        for value in test_values:
            username_field = self.driver.find_element(By.ID, "user-name")
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "login-button")
            
            username_field.clear()
            password_field.clear()
            
            username_field.send_keys(value)
            password_field.send_keys(value)
            login_button.click()
            
            time.sleep(1)
            
            error_message_elements = self.driver.find_elements(By.CLASS_NAME, "error-message-container")
            if error_message_elements:
                print(f"Boundary Test with input '{value}': Error message displayed as expected.")
            else:
                print(f"Boundary Test with input '{value}': No error message displayed.")
       
    
    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        
        time.sleep(2)
        
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys(username)
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        
        time.sleep(2)
    
    def boundary_checkout_testing(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        time.sleep(2)
        
        test_values = ["", "A"]
        
        for value in test_values:
            first_name_field = self.driver.find_element(By.ID, "first-name")
            last_name_field = self.driver.find_element(By.ID, "last-name")
            postal_code_field = self.driver.find_element(By.ID, "postal-code")
            continue_button = self.driver.find_element(By.ID, "continue")
            
            first_name_field.clear()
            last_name_field.clear()
            postal_code_field.clear()
            
            first_name_field.send_keys(value)
            last_name_field.send_keys(value)
            postal_code_field.send_keys(value)
            continue_button.click()
            
            time.sleep(1)
            
            error_message_elements = self.driver.find_elements(By.CLASS_NAME, "error-message-container")
            if error_message_elements:
                print(f"Boundary Test for checkout input '{value}': Error message displayed as expected.")
            else:
                print(f"Boundary Test for checkout input '{value}': No error message displayed.")
    
    def test_checkout_button(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(2)
        
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        
        time.sleep(2)
        
        assert "checkout-step-one.html" in self.driver.current_url, "Checkout page did not open."
        print("Checkout page opened successfully.")
        
        first_name_field = self.driver.find_element(By.ID, "first-name")
        last_name_field = self.driver.find_element(By.ID, "last-name")
        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        
        first_name_field.send_keys("John")
        last_name_field.send_keys("Doe")
        postal_code_field.send_keys("12345")
        
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        
        time.sleep(2)
        
        assert "checkout-step-two.html" in self.driver.current_url, "Checkout step two did not open."
        print("Proceeded to checkout step two successfully.")
        
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        
        time.sleep(2)
        
        assert "checkout-complete.html" in self.driver.current_url, "Checkout completion page did not open."
        print("Checkout completed successfully.")
        
        back_to_products = self.driver.find_element(By.ID, "back-to-products")
        back_to_products.click()
        
        assert "inventory.html" in self.driver.current_url, "main page did not open"
        print("main page opened successfully.")
        
        time.sleep(2)
        

    def test_add_to_cart_button(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        time.sleep(2)
        
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
        
        time.sleep(2)
        
        cart_quantity = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert int(cart_quantity.text) > 0, "Cart quantity is 0, test failed."
        print("Item successfully added to cart. Test passed.")
        
        continue_shopping_button = self.driver.find_element(By.ID, "continue-shopping")
        continue_shopping_button.click()
        
        time.sleep(2)
        print("Returned to inventory page.")
        
    
    def test_remove_item_from_cart(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        time.sleep(2)
        
        remove_button = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_button.click()
        
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
        
        time.sleep(2)
        
        cart_badge_elements = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(cart_badge_elements) == 0, "Cart is not empty, test failed."
        print("Item successfully removed from cart. Test passed.")
        

        
    def test_open_product_details(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        time.sleep(2)
        
        product_link = self.driver.find_element(By.ID, "item_4_title_link")
        product_link.click()
        
        time.sleep(2)
        
        assert "inventory-item.html" in self.driver.current_url, "Product details page did not open."
        print("Product details page opened successfully.")
        
        back_button = self.driver.find_element(By.ID, "back-to-products")
        back_button.click()
        
        time.sleep(2)
        
        assert "inventory.html" in self.driver.current_url, "Did not return to product list."
        print("Successfully returned to product list.")
        
    
    def usability_test_product_sort_container(self):
        sort_container = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert sort_container.is_displayed(), "Product sort container is not visible."
        print("Product sort container is visible.")
        
        
    def test_social_networks_footer(self):
        social_links = ["twitter", "facebook", "linkedin"]
        for network in social_links:
            link = self.driver.find_element(By.CLASS_NAME, f"social_{network}")
            assert link.is_displayed(), f"{network} link is not visible."
            print(f"{network.capitalize()} link is visible.")
    
    def usability_testing(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            assert button.is_displayed() and button.is_enabled(), f"Button {button.text} is not usable."
        print("All buttons are accessible and usable.")
    
    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    test = SauceDemoTest()
    
    test.performance_testing()
    
    test.boundary_login_testing()
    
    test.login("standard_user", "secret_sauce")
    
    test.boundary_checkout_testing()
    test.test_checkout_button()
    
    test.test_add_to_cart_button()
    test.test_remove_item_from_cart()
    
    test.test_open_product_details()
    
    
    test.usability_test_product_sort_container()
    test.test_social_networks_footer()
    test.usability_testing()
    test.close()
