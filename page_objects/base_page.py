from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from utils.read_properties import ReadConfig
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on element: {by_locator}")
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    @allure.step("Send keys '{text}' to element: {by_locator}")
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_clickable(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            return True
        except TimeoutException:
            return False

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def is_visible(self, by_locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def is_present(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def wait_for_element_to_disappear(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def get_attribute_value(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute)

    def scroll_into_view(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def open_homepage(self):
        self.driver.get(ReadConfig.get_app_url())

    @allure.step("Click with JavaScript on element: {by_locator}")
    def click_with_js(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        self.driver.execute_script("arguments[0].click();", element)

    def get_elements(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))

    def is_text_present(self, text):
        return text in self.driver.page_source

    @allure.step("Click on element and validate navigation to new tab")
    def click_and_validate_new_tab(self, click_locator, expected_urls, timeout=10):
        """
        Clicks on an element, switches to new tab, validates the URL, and switches back.

        :param click_locator: Tuple of (By.XPATH, "xpath_value")
        :param expected_urls: List of expected URLs to validate
        :param timeout: Timeout for waiting
        """
        main_window = self.driver.current_window_handle

        # Click the element
        self.do_click(click_locator)

        # Wait for new tab to open
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)
        new_window = [handle for handle in self.driver.window_handles if handle != main_window][0]

        # Switch to new tab
        self.driver.switch_to.window(new_window)

        # Validate URL
        with allure.step("Validate the URL of the new tab"):
            current_url = self.driver.current_url
            assert any(url in current_url for url in expected_urls), f"Expected one of {expected_urls}, but got {current_url}"

        # Close new tab
        self.driver.close()

        # Switch back to main window
        self.driver.switch_to.window(main_window)