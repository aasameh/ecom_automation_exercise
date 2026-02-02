from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import on_home_page
from pages.home_page import HomePage
from pages.login_page import LoginPage

scenarios('../features/register_existing_email.feature')

@when("I click on 'Signup / Login' button")
def click_signup_login(browser: WebDriver, registered_account):
    HomePage(browser).click_signup_login_btn()

@then("'New User Signup!' should be visible")
def signup_visible(browser: WebDriver):
    assert LoginPage(browser).is_new_user_signup_visible()

@when("I enter name and already registered email address")
def enter_existing_email(browser: WebDriver, registered_account):
    LoginPage(browser).signup("testuser", registered_account["email"])

@when("I click 'Signup' button")
def click_signup(browser: WebDriver):
    pass  # Already clicked in signup() method

@then("error 'Email Address already exist!' should be visible")
def error_visible(browser: WebDriver):
    assert LoginPage(browser).is_email_exists_error_visible()
