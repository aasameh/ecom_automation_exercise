from pytest_bdd import scenarios, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from conftest import on_home_page
from pages.home_page import HomePage
from pages.cart_page import CartPage
import random

scenarios('../features/subscription_home.feature')

@when("I scroll down to footer")
def scroll_to_footer(browser: WebDriver):
    CartPage(browser).scroll_to_footer()

@then("text 'SUBSCRIPTION' should be visible")
def subscription_visible(browser: WebDriver):
    assert CartPage(browser).is_subscription_visible()

@when("I enter email address in input and click arrow button")
def subscribe_with_email(browser: WebDriver):
    email = f"test{random.randint(1000, 9999)}@example.com"
    CartPage(browser).subscribe_with_email(email)  

@then("success message 'You have been successfully subscribed!' should be visible")
def subscription_success_visible(browser: WebDriver):
    assert CartPage(browser).is_subscription_success_visible()
