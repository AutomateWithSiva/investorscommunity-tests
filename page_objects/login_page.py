from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.read_properties import ReadConfig

class LoginPage(BasePage):
    EMAIL_INPUT_ID = (By.ID, "Email")
    PASSWORD_INPUT_ID = (By.ID, "Password")
    LOGIN_BUTTON_XPATH = (By.XPATH, "//button[@type='submit']")
    LOGOUT_LINK_TEXT = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ReadConfig.get_app_url())

    def set_email(self, email):
        self.do_send_keys(self.EMAIL_INPUT_ID, email)
        # self.driver.find_element(By.ID, self.EMAIL_INPUT_ID).clear()
        # self.driver.find_element(By.ID, self.EMAIL_INPUT_ID).send_keys(email)

    def set_password(self, password):
        self.do_send_keys(self.EMAIL_INPUT_ID, password)
        # self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID).clear()
        # self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID).send_keys(password)

    def click_login(self):
        self.do_click(self.LOGIN_BUTTON_XPATH)
        # self.driver.find_element(By.XPATH, self.LOGIN_BUTTON_XPATH).click()

    def click_logout(self):
        self.do_click(self.LOGOUT_LINK_TEXT)
        # self.driver.find_element(By.LINK_TEXT, self.LOGOUT_LINK_TEXT).click()


