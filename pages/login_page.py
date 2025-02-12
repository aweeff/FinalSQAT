from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SauceDemoTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
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
        
        time.sleep(5)
    
    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    test = SauceDemoTest()
    test.login("standard_user", "secret_sauce")
    test.close()
