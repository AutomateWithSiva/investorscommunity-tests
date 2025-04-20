from test_cases.test_base import BaseTest
from page_objects.login_page import LoginPage
from utils.read_properties import ReadConfig

class TestLogin(BaseTest):
    base_url = ReadConfig.get_app_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_login_title(self):
        login_page = LoginPage(self.driver)
        title = login_page.get_title('nopCommerce demo store. Login')
        assert title == 'nopCommerce demo store. Login'
        # driver.save_screenshot('../screenshots/test_login.png')

    def test_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.set_email(self.email)
        login_page.set_password(self.password)
        login_page.click_login()

        # assert driver.title == 'Dashboard / nopCommerce administration'

        login_page.click_logout()






