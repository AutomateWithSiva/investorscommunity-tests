from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.read_properties import ReadConfig
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import allure

class ReitsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    REITS_PAGE_HEADER_XPATH = (By.XPATH, "//p[contains(normalize-space(.), 'REITs and InvITs') and contains(normalize-space(.), 'price comparison with NAVs')]")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    TABLE_HEADERS = (By.CSS_SELECTOR, "table thead th")
    COLUMN_DATA = lambda self, col_index: (By.CSS_SELECTOR, f"table tbody tr td:nth-child({col_index})")
    SOURCE_BUTTONS = (By.CSS_SELECTOR, "table tbody tr td:last-child button")
    LOADING_LOCATOR = (By.XPATH, "//*[contains(text(), 'Digging the market to get current data')]")
    # Add more locators as needed (e.g., NAV tables, links, buttons)

    def is_reits_header_visible(self):
        return self.is_visible(self.REITS_PAGE_HEADER)

    def get_header_texts(self):
        return [header.text for header in self.driver.find_elements(*self.TABLE_HEADERS)]

    def get_row_count(self):
        return len(self.driver.find_elements(*self.TABLE_ROWS))

    def get_column_values(self, col_index):
        return [elem.text for elem in self.driver.find_elements(*self.COLUMN_DATA(col_index))]

    def are_all_source_buttons_clickable(self):
        buttons = self.driver.find_elements(*self.SOURCE_BUTTONS)

        main_window = self.driver.current_window_handle
        errors = []

        for index, button in enumerate(buttons):
            # Open in new tab
            ActionChains(self.driver).move_to_element(button).click().perform()

            try:
                WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
                new_window = [w for w in self.driver.window_handles if w != main_window][0]
                self.driver.switch_to.window(new_window)

                current_url = self.driver.current_url
                if not current_url.lower().endswith(".pdf"):
                    errors.append(f"[Button {index + 1}] URL does not end with .pdf: {current_url}")
                    continue

                # ✅ Check if it's rendered using <embed> or <iframe>
                embed_exists = len(self.driver.find_elements(By.TAG_NAME, "embed")) > 0
                iframe_exists = len(self.driver.find_elements(By.TAG_NAME, "iframe")) > 0

                if not (embed_exists or iframe_exists):
                    errors.append(
                        f"[Button {index + 1}] PDF not visibly rendered (no embed/iframe found). URL: {current_url}")

            except Exception as e:
                errors.append(f"[Button {index + 1}] Exception occurred: {str(e)}")

            finally:
                self.driver.close()
                self.driver.switch_to.window(main_window)

        return errors

    def wait_for_loading_to_disappear(self):
        """Wait for the loading message to disappear."""
        return self.wait_for_element_to_disappear(self.LOADING_LOCATOR)



