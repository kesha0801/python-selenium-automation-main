from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    # SIGN_IN = (By.XPATH, "//span[text()='Sign in']")
    # SIGN_IN_SIDE_NAV = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    #def search_product(self):
    #self.input_text('coffee', *self.SEARCH_FIELD)

    def search_product(self, product):
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)
