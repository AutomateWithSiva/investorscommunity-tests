from test_cases.test_base import BaseTest
from page_objects.navbar_page import NavBar
import allure

@allure.feature("Nav Bar")
@allure.story("Verify Nav Bar Navigations")
class TestNavBar(BaseTest):

    @allure.title("Test Navbar Links Visibility and Navigation")
    @allure.description("Validate if IPOs, Arbitrage, REITs, and Alts links are visible and navigable from the Navbar.")
    def test_navbar_links(self):
        navbar = NavBar(self.driver)
        navbar.open_homepage()

        with allure.step("Click IPO link and validate navigation"):
            navbar.nav_to_ipo_page()
            assert "ipo" in self.driver.current_url.lower(), "Navigation to IPO page failed"

        with allure.step("Click Arbitrage link and validate navigation"):
            navbar.nav_to_arbitrage_page()
            assert "arbitrage" in self.driver.current_url.lower(), "Navigation to Arbitrage page failed"

        with allure.step("Click REITs link and validate navigation"):
            navbar.nav_to_reits_page()
            assert "reits" in self.driver.current_url.lower(), "Navigation to REITs page failed"

        with allure.step("Click Alts link and validate navigation"):
            navbar.nav_to_alts_page()
            assert "alts" in self.driver.current_url.lower(), "Navigation to Alts page failed"

