from selenium.webdriver.remote.webdriver import WebDriver
from pytest_bdd import scenarios, given, when, then
from conftest import on_home_page
from pages.home_page import HomePage

scenarios('../features/test_cases_page.feature')

@when("I click on 'Test Cases' button")
def click_test_cases(browser: WebDriver):
    HomePage(browser).click_test_cases_btn()

@then("user should be navigated to test cases page successfully")
def on_test_cases_page(browser: WebDriver):
    assert "/test_cases" in browser.current_url