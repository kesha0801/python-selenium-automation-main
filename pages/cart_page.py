from selenium.webdriver.common.by import By
from pages.header import Header
from pages.base_page import Page
from time import sleep


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    SIDE_NAV_ADD_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    CART_ITEM_TITLE = (By.XPATH, "//h4[contains(text(),'#2 Wood Pencils 24ct')]")
    SEARCH_FIELD = (By.ID, 'search')

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def add_to_cart_button(self):
        elements = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if elements:
            first_element = elements[0]
            first_element.click()

            self.wait_and_click(*self.SIDE_NAV_ADD_CART_BTN)
        else:
            print("No elements found")

    def verify_correct_product_in_cart(self):
        target_element = self.driver.find_elements(*self.CART_ITEM_TITLE)
        for i in range (len(target_element)):
            target_element = self.driver.find_elements(*self.CART_ITEM_TITLE)
            print(f'Clicking on element {target_element[i].text}')
            target_element[i].click()
            sleep(4)

        # if elements:
        #     if len(elements) > 1:
        #         target_element = elements[1]
        #         target_element.click()
        #     else:
        #         print("Correct product not found")

        #self.verify_text(*self.CART_ITEM_TITLE)
        #print(f'Actual product in cart name: {target_element.text}')
        #self.verify_text(self, '{search_product}', *self.SEARCH_FIELD)




