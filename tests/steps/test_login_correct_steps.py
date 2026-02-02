from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import on_home_page
from pages.home_page import HomePage
from pages.login_page import LoginPage

scenarios('../features/login_correct.feature')

@given("I am a registered user")
def have_registered_account(registered_account):
    pass

@when("I click on 'Signup / Login' button")
def click_signup_login_button(browser: WebDriver, registered_account):
    HomePage(browser).click_signup_login_btn()

@then("'Login to your account' should be visible")
def login_account_visible(browser: WebDriver, registered_account):
    assert LoginPage(browser).is_login_visible()

@when("I enter correct email address and password")
def enter_credentials(browser: WebDriver, registered_account):
    LoginPage(browser).login(registered_account["email"], registered_account["password"])

@when("I click 'login' button")
def click_login_button(browser: WebDriver):
    pass  # Already clicked in login() method

@then("'Logged in as username' should be visible")
def login_username_visible(browser: WebDriver):
    assert HomePage(browser).is_logged_in()