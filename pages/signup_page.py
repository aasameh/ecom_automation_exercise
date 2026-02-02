from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class SignupPage(BasePage):
    # Account Information
    GENDER_MR = (By.CSS_SELECTOR, "#uniform-id_gender1")
    GENDER_MRS = (By.CSS_SELECTOR, "#uniform-id_gender2")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    DAYS = (By.CSS_SELECTOR, "#days")
    MONTHS = (By.CSS_SELECTOR, "#months")
    YEARS = (By.CSS_SELECTOR, "#years")
    NEWSLETTER = (By.CSS_SELECTOR, "#newsletter")
    OPTIN = (By.CSS_SELECTOR, "#optin")

    # Address Information
    FIRST_NAME = (By.CSS_SELECTOR, "#first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#last_name")
    COMPANY = (By.CSS_SELECTOR, "#company")
    ADDRESS1 = (By.CSS_SELECTOR, "#address1")
    ADDRESS2 = (By.CSS_SELECTOR, "#address2")
    COUNTRY = (By.CSS_SELECTOR, "#country")
    STATE = (By.CSS_SELECTOR, "#state")
    CITY = (By.CSS_SELECTOR, "#city")
    ZIPCODE = (By.CSS_SELECTOR, "#zipcode")
    MOBILE_NUMBER = (By.CSS_SELECTOR, "#mobile_number")

    # Buttons
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, '[data-qa="create-account"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, '[data-qa="continue-button"]')

    # Messages
    ACCOUNT_CREATED_TXT = (By.XPATH, "//*[contains(text(), 'Account Created!')]")
    ACCOUNT_DELETED_TXT = (By.XPATH, "//*[contains(text(), 'Account Deleted!')]")

    def fill_account_details(self, password: str, day: str = "1", month: str = "1", year: str = "2001"):
        self.driver.find_element(*self.GENDER_MR).click()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        Select(self.driver.find_element(*self.DAYS)).select_by_value(day)
        Select(self.driver.find_element(*self.MONTHS)).select_by_value(month)
        Select(self.driver.find_element(*self.YEARS)).select_by_value(year)

    def select_newsletter(self):
        self.driver.find_element(*self.NEWSLETTER).click()

    def select_optin(self):
        self.driver.find_element(*self.OPTIN).click()

    def fill_address_details(self, first_name: str = "Test", last_name: str = "User", 
                              company: str = "TestCompany", address1: str = "123 Test St",
                              address2: str = "Apt 1", country: str = "India",
                              state: str = "TestState", city: str = "TestCity", 
                              zipcode: str = "12345", mobile: str = "1234567890"):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.COMPANY).send_keys(company)
        self.driver.find_element(*self.ADDRESS1).send_keys(address1)
        self.driver.find_element(*self.ADDRESS2).send_keys(address2)
        Select(self.driver.find_element(*self.COUNTRY)).select_by_value(country)
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.ZIPCODE).send_keys(zipcode)
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys(mobile)

    def click_create_account(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_BTN).click()

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def is_account_created_visible(self) -> bool:
        return self.driver.find_element(*self.ACCOUNT_CREATED_TXT).is_displayed()

    def is_account_deleted_visible(self) -> bool:
        return self.driver.find_element(*self.ACCOUNT_DELETED_TXT).is_displayed()
