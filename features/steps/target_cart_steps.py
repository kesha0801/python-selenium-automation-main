from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait



ADDED_TO_CART_HEADER = (By.XPATH, "//span[text()='Added to cart']")


@then("Click add to cart")
def add_to_cart(context):
    sleep(5)  # This step won't work without sleep
    context.app.cart_page.add_to_cart_button()


    # WebDriverWait(context.driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[text()='Added to cart']"))
    # )


# @then("Verify cart has pencil")
# def cart_has_pencil(context):
#     expected_text = 'Added to cart'
#     #actual_text = context.driver.find_element(By.XPATH, "//span[text()='Added to cart']")
#     actual_text = context.driver.wait.until(EC.presence_of_element_located(ADDED_TO_CART_HEADER))
#     assert expected_text in actual_text.text


CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")



@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_correct_product_in_cart()
    #assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    # expected_text = 'Your cart is empty'
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    # assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
    context.app.cart_page.verify_cart_empty()