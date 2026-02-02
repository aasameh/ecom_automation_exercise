from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import on_home_page
from pages.home_page import HomePage
from pages.login_page import LoginPage

scenarios('../features/logout.feature')

@when("I click on 'Signup / Login' button")
def click_signup_login(browser: WebDriver, registered_account):
    HomePage(browser).click_signup_login_btn()

@then("'Login to your account' should be visible")
def login_visible(browser: WebDriver):
    assert LoginPage(browser).is_login_visible()

@when("I enter correct email address and password")
def enter_credentials(browser: WebDriver, registered_account):
    LoginPage(browser).login(registered_account["email"], registered_account["password"])

@when("I click 'login' button")
def click_login(browser: WebDriver):
    pass  # Already clicked in login() method

@then("'Logged in as username' should be visible")
def logged_in_visible(browser: WebDriver):
    assert HomePage(browser).is_logged_in()

@when("I click 'Logout' button")
def click_logout(browser: WebDriver):
    HomePage(browser).click_logout_btn()

@then("user should be navigated to login page")
def on_login_page(browser: WebDriver):
    assert "/login" in browser.current_url
