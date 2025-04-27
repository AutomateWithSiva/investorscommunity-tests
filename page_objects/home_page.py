from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.read_properties import ReadConfig
import allure

class HomePage(BasePage):
    LOGO_LINK_XPATH = (By.XPATH, "//a[@href='/' and .//h3[text()='Investors'] and .//h3[text()='Community']]")
    DESCRIPTION_XPATH = (By.XPATH, "//p[contains(text(), 'Investors Community helps you to find new opportunities in Indian market to invest')]")

    WHATSAPP_CARD_XPATH = (By.XPATH, "//h4[text()='Whatsapp Community']/parent::div/parent::div")
    WHATSAPP_TITLE_XPATH = (By.XPATH, "//h4[text()='Whatsapp Community']")
    WHATSAPP_DESCRIPTION_1 = (By.XPATH, "//p[text()='To Share thoughts']")
    WHATSAPP_DESCRIPTION_2 = (By.XPATH, "//p[text()='and get notified about new stuffs']")
    WHATSAPP_JOIN_BUTTON_XPATH = (By.XPATH, "//h4[text()='Whatsapp Community']/parent::div/parent::div//button[text()='JOIN NOW']")

    TWITTER_CARD_XPATH = (By.XPATH, "//h4[text()='Twitter Community']/parent::div/parent::div")
    TWITTER_TITLE_XPATH = (By.XPATH, "//h4[text()='Twitter Community']")
    TWITTER_DESCRIPTION_1 = (By.XPATH, "//p[text()='To follow']")
    TWITTER_DESCRIPTION_2 = (By.XPATH, "//p[text()='our tweets']")
    TWITTER_FOLLOW_BUTTON_XPATH = (By.XPATH, "//h4[text()='Twitter Community']/parent::div/parent::div//button[text()='FOLLOW']")

    TELEGRAM_CARD_XPATH = (By.XPATH, "//h4[text()='Telegram Community']/parent::div/parent::div")
    TELEGRAM_TITLE_XPATH = (By.XPATH, "//h4[text()='Telegram Community']")
    TELEGRAM_DESCRIPTION_1 = (By.XPATH, "//p[text()='To exchange thoughts']")
    TELEGRAM_DESCRIPTION_2 = (By.XPATH, "//p[text()='without sharing your contact']")
    TELEGRAM_JOIN_BUTTON_XPATH = (By.XPATH, "//h4[text()='Telegram Community']/parent::div/parent::div//button[text()='JOIN NOW']")

    ALT_CARD_XPATH = (By.XPATH, "//h4[text()='Alt Platforms']/ancestor::div[contains(@class, 'flex flex-col relative')]")
    ALT_CARD_TITLE_XPATH = (By.XPATH, "//h4[text()='Alt Platforms']")
    ALT_CARD_BUTTON_XPATH = (By.XPATH, "//h4[text()='Alt Platforms']/ancestor::div[contains(@class, 'flex flex-col')]//button[text()='Try Out']")

    ARBITRAGE_CARD_XPATH = (By.XPATH, "//h4[text()='Arbitrage opportunities']/ancestor::div[contains(@class, 'flex flex-col relative')]")
    ARBITRAGE_CARD_TITLE_XPATH = (By.XPATH, "//h4[text()='Arbitrage opportunities']")
    ARBITRAGE_CARD_BUTTON_XPATH = (By.XPATH,"//h4[text()='Arbitrage opportunities']/ancestor::div[contains(@class, 'flex flex-col')]//button[text()='Try Out']")

    REITS_CARD_XPATH = (By.XPATH, "//h4[text()='REITs & InvITs Comparison']/ancestor::div[contains(@class, 'flex flex-col relative')]")
    REITS_CARD_TITLE_XPATH = (By.XPATH, "//h4[text()='REITs & InvITs Comparison']")
    REITS_CARD_BUTTON_XPATH = (By.XPATH,"//h4[text()='REITs & InvITs Comparison']/ancestor::div[contains(@class, 'flex flex-col')]//button[text()='Try Out']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ReadConfig.get_app_url())

    def is_logo_displayed(self):
        return self.is_visible(self.LOGO_LINK_XPATH)

    def get_logo_text(self):
        return self.get_element_text(self.LOGO_LINK_XPATH)

    def get_logo_href(self):
        return self.get_attribute_value(self.LOGO_LINK_XPATH, "href")

    def is_whatsapp_card_displayed(self):
        return self.is_visible(self.WHATSAPP_CARD_XPATH)

    def get_whatsapp_heading(self):
        return self.get_element_text(self.WHATSAPP_TITLE_XPATH)

    def is_join_button_clickable(self):
        return self.is_clickable(self.WHATSAPP_JOIN_BUTTON_XPATH)

    def click_wap_join_now_button(self):
        if self.is_clickable(self.WHATSAPP_JOIN_BUTTON_XPATH):
            self.do_click(self.WHATSAPP_JOIN_BUTTON_XPATH)
        else:
            raise Exception("Join Now button is not clickable")

    @allure.step("Check if Twitter card is displayed")
    def is_twitter_card_displayed(self):
        return self.is_visible(self.TWITTER_CARD_XPATH)

    @allure.step("Get Twitter card heading text")
    def get_twitter_heading(self):
        return self.get_element_text(self.TWITTER_TITLE_XPATH)

    @allure.step("Check if Follow button is clickable")
    def is_twitter_follow_button_clickable(self):
        return self.is_clickable(self.TWITTER_FOLLOW_BUTTON_XPATH)

    @allure.step("Click on Follow button in Twitter card")
    def click_twitter_follow_button(self):
        if self.is_clickable(self.TWITTER_FOLLOW_BUTTON_XPATH):
            self.do_click(self.TWITTER_FOLLOW_BUTTON_XPATH)
        else:
            raise Exception("Follow button is not clickable")

    @allure.step("Check if Telegram card is displayed")
    def is_telegram_card_displayed(self):
        return self.is_visible(self.TELEGRAM_CARD_XPATH)

    @allure.step("Get Telegram card heading text")
    def get_telegram_heading(self):
        return self.get_element_text(self.TELEGRAM_TITLE_XPATH)

    @allure.step("Check if Telegram JOIN NOW button is clickable")
    def is_telegram_join_button_clickable(self):
        return self.is_clickable(self.TELEGRAM_JOIN_BUTTON_XPATH)

    @allure.step("Click on JOIN NOW button in Telegram card")
    def click_telegram_join_now_button(self):
        if self.is_clickable(self.TELEGRAM_JOIN_BUTTON_XPATH):
            self.do_click(self.TELEGRAM_JOIN_BUTTON_XPATH)
        else:
            raise Exception("Join Now button is not clickable")

    def get_description_text(self):
        return self.get_element_text(self.DESCRIPTION_XPATH)

    @allure.step("Check if Alt Platforms card is displayed")
    def is_alt_card_displayed(self):
        return self.is_visible(self.ALT_CARD_XPATH)

    @allure.step("Get Alt Platforms card heading text")
    def get_alt_card_heading(self):
        return self.get_element_text(self.ALT_CARD_TITLE_XPATH)

    @allure.step("Check if Try Out button is clickable")
    def is_alt_try_out_button_clickable(self):
        return self.is_clickable(self.ALT_CARD_BUTTON_XPATH)

    @allure.step("Check if Arbitrage card is displayed")
    def is_arbitrage_card_displayed(self):
        return self.is_visible(self.ARBITRAGE_CARD_XPATH)

    @allure.step("Get Arbitrage card heading text")
    def get_arbitrage_card_title(self):
        return self.get_element_text(self.ARBITRAGE_CARD_TITLE_XPATH)

    @allure.step("Check if Try Out button is clickable")
    def is_arbitrage_try_out_button_clickable(self):
        return self.is_clickable(self.ARBITRAGE_CARD_BUTTON_XPATH)

    @allure.step("Check if Reits card is displayed")
    def is_reits_card_displayed(self):
        return self.is_visible(self.REITS_CARD_XPATH)

    @allure.step("Get Reits card heading text")
    def get_reits_card_title(self):
        return self.get_element_text(self.REITS_CARD_TITLE_XPATH)

    @allure.step("Check if Try Out button is clickable")
    def is_reits_try_out_button_clickable(self):
        return self.is_clickable(self.REITS_CARD_BUTTON_XPATH)



