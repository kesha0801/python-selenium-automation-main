from selenium.webdriver.common.by import By

from pages.base_page import Page


class PrivacyPage(Page):

    T_C_PAGE_OPENED = (By.CSS_SELECTOR, "[data-test='page-title']")

    def verify_pp_url(self):
        self.verify_partial_url('/target-privacy-policy')

    def verify_t_c_opened(self):
        #actual_text = self.driver.find_element(*self.T_C_PAGE_OPENED)
        self.verify_partial_text('terms & conditions', *self.T_C_PAGE_OPENED)

