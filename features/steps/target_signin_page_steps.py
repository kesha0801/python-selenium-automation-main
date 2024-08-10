from selenium.webdriver.common.by import By
from behave import given, when, then


#Homework 7 testcases below:

@then('Click sign in button on header')
def sign_in(context):
    context.app.signin_page.sign_in_button()


@then('Click sign in button on side nav')
def sign_in_side_nav(context):
    context.app.signin_page.sign_in_side_nav()


@then('Verify sign in page is open')
def sign_in_page(context):
    context.app.signin_page.sign_in_confirmation()

