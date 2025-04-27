from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.read_properties import ReadConfig
import allure

class ReitsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    REITS_PAGE_HEADER_XPATH = (By.XPATH, "//p[contains(normalize-space(.), 'REITs and InvITs') and contains(normalize-space(.), 'price comparison with NAVs')]")
    # Add more locators as needed (e.g., NAV tables, links, buttons)

    def is_reits_header_visible(self):
        return self.is_visible(self.REITS_PAGE_HEADER)