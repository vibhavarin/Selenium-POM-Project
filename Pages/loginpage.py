from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginPage:
    url = 'https://the-internet.herokuapp.com/login'

    username = 'id','username'
    password = 'id','password'
    login_button = 'xpath','//button[@type="submit"]'
    logout_button = 'xpath','//a[@class="button secondary radius"]'
    success_message = 'css selector','.flash.success'
    error_message = 'css selector','.flash.error'

    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.get(self.url)
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()


    def popup_close(self):
        self.driver.switch_to.active_element.send_keys(Keys.TAB)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def get_successful_login(self):
        return self.driver.find_element(*self.success_message).text

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def logout(self):
        self.driver.find_element(*self.logout_button).click()