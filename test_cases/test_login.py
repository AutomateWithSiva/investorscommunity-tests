from page_objects.login_page import LoginPage
from utils.read_properties import ReadConfig

class TestLogin:
    base_url = ReadConfig.get_app_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_login_title(self, setup):
        driver = setup
        driver.get(self.base_url)
        title = driver.title
        assert title == 'nopCommerce demo store. Login'
        driver.save_screenshot('../screenshots/test_login.png')

    def test_login_page(self, setup):
        driver = setup
        driver.get(self.base_url)
        login_page = LoginPage(driver)

        login_page.set_email(self.email)
        login_page.set_password(self.password)
        login_page.click_login()

        # assert driver.title == 'Dashboard / nopCommerce administration'

        login_page.click_logout()
        driver.close()






