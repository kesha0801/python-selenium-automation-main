from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class TargetAppPage(Page):
    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")
    #TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")
    #TC_LINK = (By.XPATH, "//a[contains (@href, '/c/terms-conditions/')]")
    TC_LINK = (By.CSS_SELECTOR, 'a[href*="/c/terms-conditions"][target="_blank"]')

    def open_target_app(self):
        self.open_url('https://www.target.com/c/target-app/')

    def click_pp_link(self):
        self.click(*self.PP_LINK)

    def click_t_c_link(self):
        # tc_links = self.driver.find_elements(*self.TC_LINK)
        # if tc_links:
        #
        #     tc_link = tc_links[0]
        #     tc_link.click()
        self.click(*self.TC_LINK)
        #self.wait_and_click(*self.TC_LINK)
        sleep(5)





