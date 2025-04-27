from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.read_properties import ReadConfig
import allure

class NavBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    EQUITY_BUTTON_XPATH = (By.XPATH, "//button[contains(., 'Equity')]")
    IPO_LINK_XPATH = (By.XPATH, "//a[contains(., 'IPO')]")
    ARBITRAGE_LINK_XPATH = (By.XPATH, "//a[contains(., 'Arbitrage')]")
    REITS_LINK_XPATH = (By.XPATH, "//a[contains(., 'REITs')]")
    ALTS_LINK_XPATH = (By.XPATH, "//a[text()='Alts']")

    def nav_to_ipo_page(self):
        self.do_click(self.EQUITY_BUTTON_XPATH)
        self.do_click(self.IPO_LINK_XPATH)

    def nav_to_arbitrage_page(self):
        self.do_click(self.EQUITY_BUTTON_XPATH)
        self.do_click(self.ARBITRAGE_LINK_XPATH)

    def nav_to_reits_page(self):
        self.do_click(self.EQUITY_BUTTON_XPATH)
        self.do_click(self.REITS_LINK_XPATH)

    def nav_to_alts_page(self):
        self.do_click(self.ALTS_LINK_XPATH)