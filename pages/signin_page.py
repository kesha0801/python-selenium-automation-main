from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Signin(Page):
    SIGN_IN_BUTTON = (By.XPATH, "//span[text()='Sign in']")
    SIGN_IN_SIDE_NAV = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    SIGN_IN_PAGE_IS_OPENED = (By.XPATH, "//span[text()='Sign into your Target account']")

    def sign_in_button(self):
        self.wait_and_click(*self.SIGN_IN_BUTTON)

    def sign_in_side_nav(self):
        self.wait_and_click(*self.SIGN_IN_SIDE_NAV)

    def sign_in_confirmation(self):
        self.wait_and_click(*self.SIGN_IN_PAGE_IS_OPENED)










