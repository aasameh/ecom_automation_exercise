from pytest_bdd import given, when, then, scenarios
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import random
from conftest import on_home_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

scenarios('../features/signup.feature')
# "I am on the home page" step is defined in conftest.py

@when("I click on 'Signup / Login' button")
def click_signup_login_button(browser: WebDriver): 
    HomePage(browser).click_signup_login_btn()

@then("'New User Signup!' should be visible")
def signup_visible(browser: WebDriver): 
    assert LoginPage(browser).is_new_user_signup_visible()

@when("I sign up")
def enter_name_email(browser: WebDriver):
    name = f"test{random.randint(1000, 9999)}"
    email = f"test{random.randint(1000, 9999)}@test.com"
    LoginPage(browser).signup(name, email)

@then("'ENTER ACCOUNT INFORMATION' should be visible") 
def account_information_visible(browser: WebDriver):
    assert LoginPage(browser).is_enter_account_information_visible()

@when("I fill details: Title, Password, Date of birth") 
def fill_details(browser: WebDriver):
    SignupPage(browser).fill_account_details("testpassword")

@when("I Select checkbox 'Sign up for our newsletter!'") 
def select_newsletter(browser: WebDriver):
    SignupPage(browser).select_newsletter()

@when("I Select checkbox 'Receive special offers from our partners!'")
def select_optin(browser: WebDriver):
    SignupPage(browser).select_optin()

@when("I Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number") 
def fill_address_details(browser: WebDriver):
    SignupPage(browser).fill_address_details(
        first_name="first",
        last_name="last",
        company="company",
        address1="address1",
        address2="address2",
        country="India",
        state="state",
        city="city",
        zipcode="zipcode",
        mobile="123456789"
    )

@when("I Click 'Create Account button'") 
def click_create_account(browser: WebDriver):
    SignupPage(browser).click_create_account()

@then("'ACCOUNT CREATED!' should be visible") 
def account_created_visible(browser: WebDriver):
    assert SignupPage(browser).is_account_created_visible()

@when("I Click 'Continue' button")
@then("I Click 'Continue' button")
def continue_button(browser: WebDriver):
    SignupPage(browser).click_continue()

@then("'Logged in as username' should be visible") 
def login_username_visible(browser: WebDriver):
    assert HomePage(browser).is_logged_in()

@when("I Click 'Delete Account' button")
def click_delete_account(browser: WebDriver):
    HomePage(browser).click_delete_account_btn()

@then("'ACCOUNT DELETED!' should be visible")
def account_deleted_visible(browser: WebDriver):
    assert SignupPage(browser).is_account_deleted_visible()

