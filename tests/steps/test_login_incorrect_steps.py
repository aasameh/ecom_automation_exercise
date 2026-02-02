from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import on_home_page
from pages.home_page import HomePage
from pages.login_page import LoginPage

scenarios('../features/login_incorrect.feature')

@when("I click on 'Signup / Login' button")
def click_signup_login_button(browser: WebDriver):
    HomePage(browser).click_signup_login_btn()

@then("'Login to your account' should be visible")
def login_account_visible(browser: WebDriver):
    assert LoginPage(browser).is_login_visible()

@when("I enter incorrect email address and password")
def enter_credentials(browser: WebDriver):
    LoginPage(browser).login("incorrect@gmail", "incorrectpassword")

@when("I click 'login' button")
def click_login_button(browser: WebDriver):
    pass  # Already clicked in login() method

@then("error 'Your email or password is incorrect!' should be visible")
def login_error_visible(browser: WebDriver):
    assert LoginPage(browser).is_login_error_visible()