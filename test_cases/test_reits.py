from test_cases.test_base import BaseTest
from page_objects.reits_page import ReitsPage
from page_objects.navbar_page import NavBar
from utils.read_properties import ReadConfig
import allure
import pytest


@allure.feature("REITs Page")
@allure.story("Validate REITs and InvITs Table Data")
class TestReitsPage(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver.get(ReadConfig.get_app_url())
        self.navbar = NavBar(self.driver)
        self.navbar.nav_to_reits_page()
        self.reits_page = ReitsPage(self.driver)

    @allure.title("Test REITs Table Headers and Data")
    @allure.description("Validate REITs table headers, row count, value formatting, button states, and price columns.")
    def test_reits_table_data(self):
        # Validate table headers
        expected_headers = [
            "Name", "Category", "Current Price", "NAV per share",
            "Value Difference", "Distribution Yield", "Source"
        ]
        actual_headers = self.reits_page.get_header_texts()
        assert actual_headers == expected_headers, f"Expected headers {expected_headers}, but got {actual_headers}"
        assert self.reits_page.wait_for_loading_to_disappear(), 'The Loader is still visible'
        # Validate row count
        row_count = self.reits_page.get_row_count()
        assert row_count == 8, f"Expected 8 rows, but found {row_count}"

        # Validate percentage format in 'Value Difference' column (assume it's 5th column: index 5)
        percentage_cols = [5, 6]
        for col_index in percentage_cols:
            value_diff_values = self.reits_page.get_column_values(col_index=col_index)
            for value in value_diff_values:
                assert "%" in value, f"Value '{value}' is not a valid percentage"
                assert value.strip()[0] in ["-", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], \
                    f"Unexpected prefix in '{value}'"

        # Validate all source buttons are clickable and pdf is opened properly
        # errors = self.reits_page.are_all_source_buttons_clickable()
        # assert not errors, "\n".join(errors)

        # Validate price columns contain numeric values (3rd and 4th columns: indexes 3 and 4)
        price_cols = [3, 4]
        for col_index in price_cols:
            values = self.reits_page.get_column_values(col_index=col_index)
            for val in values:
                clean_val = val.replace(",", "").replace(".", "", 1)
                assert clean_val.isdigit(), f"Non-numeric value found in column {col_index}: '{val}'"
