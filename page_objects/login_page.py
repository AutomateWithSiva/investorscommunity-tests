from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL_INPUT_ID = "Email"
    PASSWORD_INPUT_ID = "Password"
    LOGIN_BUTTON_XPATH = "//button[@type='submit']"
    LOGOUT_LINK_TEXT = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.EMAIL_INPUT_ID).clear()
        self.driver.find_element(By.ID, self.EMAIL_INPUT_ID).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID).clear()
        self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON_XPATH).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.LOGOUT_LINK_TEXT).click()


