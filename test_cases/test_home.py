from test_cases.test_base import BaseTest
from page_objects.home_page import HomePage
from utils.read_properties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from config import expected_links
import allure

@allure.feature("Home Page")
@allure.story("Verify WhatsApp Community Card Section")
class TestHome(BaseTest):
    base_url = ReadConfig.get_app_url()

    @allure.title("Verify Home Page Title")
    @allure.description("Ensure that the page title is 'Investors Community'")
    def test_home_title(self):
        home = HomePage(self.driver)
        with allure.step("Get the page title"):
            title = home.get_title('Investors Community')
            assert title == 'Investors Community', f"Expected title to be 'Investors Community' but got '{title}'"

    @allure.title("Verify Logo Visibility, Text and Link")
    @allure.description("Checks if the Investors Community logo is visible, has correct text, and links to home")
    def test_logo_displayed_and_text(self):
        home = HomePage(self.driver)

        with allure.step("Check if logo is displayed"):
            assert home.is_logo_displayed(), "Logo is not visible on home page"

        with allure.step("Validate logo text content"):
            logo_text = home.get_logo_text()
            assert "Investors" in logo_text and "Community" in logo_text, f"Logo text is incorrect: {logo_text}"

        with allure.step("Validate logo href link"):
            logo_href = home.get_logo_href()
            assert logo_href.endswith("/"), f"Logo link should point to '/', but got '{logo_href}'"

        with allure.step("Verify the description text"):
            description_text = home.get_description_text()

            expected_description = (
                "Investors Community helps you to find new opportunities in Indian market to invest. "
                "We just curate the various information available online and provide you in easy format to make use of it. "
                "All the information provided in the site are just for educational purpose and not an Investment advice. "
                "Do your own research before doing any investments."
            )

            with allure.step("Verify the description text matches expected content"):
                assert description_text == expected_description, f"Expected description: {expected_description}, but got: {description_text}"

    @allure.title("Verify WhatsApp Community card is displayed correctly")
    @allure.description("Checks the WhatsApp card, heading, descriptions, and JOIN NOW button")
    def test_whatsapp_community_card(self):
        home = HomePage(self.driver)

        with allure.step("Verify WhatsApp card is visible"):
            assert home.is_whatsapp_card_displayed(), "WhatsApp Community card not visible"

        with allure.step("Verify card heading is correct"):
            assert "Whatsapp Community" in home.get_whatsapp_heading(), "Incorrect heading"

        with allure.step("Verify description lines are present"):
            assert home.is_present(HomePage.WHATSAPP_DESCRIPTION_1), "Description line 1 missing"
            assert home.is_present(HomePage.WHATSAPP_DESCRIPTION_2), "Description line 2 missing"

        with allure.step("Validate Whatapp JOIN NOW"):
            if home.is_join_button_clickable():
                home.click_wap_join_now_button()
                main_window_handle = self.driver.current_window_handle
                WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
                new_window_handle = [handle for handle in self.driver.window_handles if handle != main_window_handle][0]
                self.driver.switch_to.window(new_window_handle)
                current_url = self.driver.current_url
                assert current_url in expected_links.WHATSAPP_COMMUNITY_LINKS, f"Expected URL: {expected_links.WHATSAPP_COMMUNITY_LINKS}, but got: {current_url}"
                self.driver.close()
                self.driver.switch_to.window(main_window_handle)
            else:
                assert False, ("The 'Join Now' button is not clickable.")

    @allure.title("Verify Twitter Community card is displayed correctly")
    @allure.description("Checks the Twitter card, heading, descriptions, and FOLLOW button")
    def test_twitter_community_card(self):
        home = HomePage(self.driver)

        with allure.step("Verify Twitter card is visible"):
            assert home.is_twitter_card_displayed(), "Twitter Community card not visible"

        with allure.step("Verify card heading is correct"):
            assert "Twitter Community" in home.get_twitter_heading(), "Incorrect heading on Twitter card"

        with allure.step("Verify description lines are present"):
            assert home.is_present(HomePage.TWITTER_DESCRIPTION_1), "Twitter description line 1 missing"
            assert home.is_present(HomePage.TWITTER_DESCRIPTION_2), "Twitter description line 2 missing"

        with allure.step("Validate Twitter FOLLOW button"):
            if home.is_twitter_follow_button_clickable():
                home.click_and_validate_new_tab(home.TWITTER_FOLLOW_BUTTON_XPATH, expected_links.TWITTER_COMMUNITY_LINK)
            else:
                assert False, "The 'Follow' button is not clickable."

    @allure.title("Verify Telegram Community card is displayed correctly")
    @allure.description("Checks the Telegram card, heading, descriptions, and JOIN NOW button")
    def test_telegram_community_card(self):
        home = HomePage(self.driver)

        with allure.step("Verify Telegram card is visible"):
            assert home.is_telegram_card_displayed(), "Telegram Community card not visible"

        with allure.step("Verify card heading is correct"):
            assert "Telegram Community" in home.get_telegram_heading(), "Incorrect heading"

        with allure.step("Verify description lines are present"):
            assert home.is_present(HomePage.TELEGRAM_DESCRIPTION_1), "Telegram description line 1 missing"
            assert home.is_present(HomePage.TELEGRAM_DESCRIPTION_2), "Telegram description line 2 missing"

        with allure.step("Validate Telegram JOIN NOW"):
            if home.is_telegram_join_button_clickable():
                home.click_and_validate_new_tab(home.TELEGRAM_JOIN_BUTTON_XPATH, expected_links.TELEGRAM_COMMUNITY_LINK)
            else:
                assert False, ("The 'Join Now' button is not clickable.")

    import allure

    @allure.title("Verify Alt Platforms card is displayed and functional")
    @allure.description("Checks Alt Platforms card visibility, title, button, and navigation")
    def test_alt_platforms_card(self):
        home = HomePage(self.driver)

        with allure.step("Verify Alt Platforms card is visible"):
            assert home.is_alt_card_displayed(), "Alt Platforms card not visible"

        with allure.step("Verify Alt Platforms card heading is correct"):
            assert "Alt Platforms" in home.get_alt_card_heading(), "Incorrect Alt Platforms heading"

        with allure.step("Click Try Out button and validate new tab navigation"):
            if home.is_alt_try_out_button_clickable():
                home.click_and_validate_new_tab(home.ALT_CARD_BUTTON_XPATH, expected_links.ALT_PAGE_LINK)
            else:
                assert False, "Try Out button not clickable"

    @allure.title("Verify Arbitrage card is displayed and functional")
    @allure.description("Checks Arbitrage card visibility, title, button, and navigation")
    def test_arb_card(self):
        home = HomePage(self.driver)

        with allure.step("Verify Arbitrage Opportunities card is visible"):
            assert home.is_arbitrage_card_displayed(), "Arbitrage Opportunities card not visible"

        with allure.step("Verify Arbitrage Opportunities card heading is correct"):
            assert "Arbitrage opportunities" in home.get_arbitrage_card_title(), "Incorrect Arbitrage Opportunities heading"

        with allure.step("Click Try Out button and validate new tab navigation"):
            if home.is_arbitrage_try_out_button_clickable():
                home.click_and_validate_new_tab(home.ARBITRAGE_CARD_BUTTON_XPATH, expected_links.ARBITRAGE_PAGE_LINK)
            else:
                assert False, "Try Out button not clickable"

    @allure.title("Verify Reits card is displayed and functional")
    @allure.description("Checks Reits card visibility, title, button, and navigation")
    def test_reits_card(self):
        home = HomePage(self.driver)

        with allure.step("Verify REITs & InvITs Comparison card is visible"):
            assert home.is_reits_card_displayed(), "REITs & InvITs Comparison card not visible"

        with allure.step("Verify REITs & InvITs Comparison card heading is correct"):
            assert "REITs & InvITs Comparison" in home.get_reits_card_title(), "Incorrect REITs & InvITs heading"

        with allure.step("Click Try Out button and validate new tab navigation"):
            if home.is_reits_try_out_button_clickable():
                home.click_and_validate_new_tab(home.REITS_CARD_BUTTON_XPATH, expected_links.REITS_PAGE_LINK)
            else:
                assert False, "Try Out button not clickable"




