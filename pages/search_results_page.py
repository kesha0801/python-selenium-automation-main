from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")

    # def verify_text(self):
    #     actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
    #     assert 'coffee' in actual_text, f'Expected coffee not in actual {actual_text}'

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    # def verify_url(self):
    #     url = self.driver.current_url
    #     assert 'coffee' in url, f'Expected "coffee" not in {url}'

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)