import time

from selenium.webdriver.common.devtools.v146.smart_card_emulation import report_error

from Pages.loginpage import LoginPage

class TestLogin:
    def test_successful_login(self, driver):
        page = LoginPage(driver)
        page.login('tomsmith','SuperSecretPassword!')
        time.sleep(3)
        page.popup_close()
        report = page.get_successful_login()
        assert 'You logged into a secure area!' in report
        print('Login successful!')


    def test_failed_login(self,driver):
        page = LoginPage(driver)
        page.login('tomsmith','SuperSecret')
        time.sleep(3)
        error= page.get_error_message()
        assert 'Your password is invalid!' in error
        print('Error detected')


    def logout(self,driver):
        page = LoginPage(driver)
        page.login('tomsmith','SuperSecretPassword!')
        time.sleep(2)
        page.popup_close()
        page.logout()
        report = page.get_error_message()
        assert 'You are logged out of the secure area!' in report
        print('logout successful!')