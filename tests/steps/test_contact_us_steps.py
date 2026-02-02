from pytest_bdd import scenarios, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from pages.contact_page import ContactPage

scenarios('../features/contact_us.feature')

@when("I click on 'Contact Us' button")
def click_contact_us(browser: WebDriver): 
    HomePage(browser).click_contact_us_btn()

@then("'GET IN TOUCH' should be visible")
def get_in_touch_visible(browser:WebDriver): 
    ContactPage(browser).is_visible(ContactPage(browser).GET_IN_TOUCH_TXT)

@when("I enter name, email, subject and message")
def enter_contact_details(browser: WebDriver):
    ContactPage(browser).enter_contact_details(
        name="Test User",
        email="test@email.com",
        subject="Test Subject",
        message="This is a test message."
    )
@when("I upload a file")
def upload_file(browser: WebDriver):
    ContactPage(browser).upload_file("C:\\work\\QA\\ecom\\tests\\resources\\test_file.txt")

@when("I click 'Submit' button")
def click_submit(browser: WebDriver):
    ContactPage(browser).click(ContactPage(browser).CONTACT_SUBMIT_BTN)

@when("I click OK button")
def click_alert_ok(browser: WebDriver):
    try:
        WebDriverWait(browser, 10).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert.accept()
    except:
        print("No alert appeared")
        pass

@then("success message 'Success! Your details have been submitted successfully.' should be visible")
def success_msg_visible(browser:WebDriver):
    ContactPage(browser).is_visible(ContactPage(browser).CONTACT_SUCCESS_MSG)

@when("I click 'Home' button")
def click_home_button(browser:WebDriver):
    ContactPage(browser).click(ContactPage(browser).CONTACT_HOME_BTN)

@then("landed to home page successfully")
def landed_home(browser:WebDriver):
    assert "Automation Exercise" in browser.title