from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Amazon logo
driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")

#Create account
driver.find_element(By.XPATH, "//h1[text()='Create account']")

#Your name field
driver.find_element(By.CSS_SELECTOR, "input[placeholder*='First']")

#Email
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#Password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

#Re-enter Password
driver.find_element(By.CSS_SELECTOR, "[name='passwordCheck']")

#Continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

#Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='customer/display.html/ref=ap_register_notification_condition_of_use']")

#Privacy Notice
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Sign in
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

#Passwords must be at least 6 characters.
driver.find_element(By.XPATH, "//div[text()='Passwords must be at least 6 characters.']")





