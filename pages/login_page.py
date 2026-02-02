from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):

    LOGIN_EMAIL = (By.CSS_SELECTOR, '[data-qa="login-email"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-qa="login-button"]')
    SIGNUP_EMAIL = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_NAME = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGNUP_BTN = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
    LOGIN_TXT = (By.XPATH, "//*[text()='Login to your account']")
    SIGNUP_TXT = (By.XPATH, "//*[contains(text(), 'New User Signup!')]")
    DETAILS_TXT = (By.XPATH, "//*[contains(text(), 'Enter Account Information')]")
    LOGIN_ERROR_TXT = (By.XPATH, "//*[text()='Your email or password is incorrect!']")
    EMAIL_EXISTS_ERROR_TXT = (By.XPATH, "//*[contains(text(), 'Email Address already exist!')]")

    def is_login_visible(self) -> bool:
        return self.driver.find_element(*self.LOGIN_TXT).is_displayed()
    
    def is_new_user_signup_visible(self) -> bool:
        return self.driver.find_element(*self.SIGNUP_TXT).is_displayed()

    def login(self, email: str, password: str):
        self.driver.find_element(*self.LOGIN_EMAIL).send_keys(email)
        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def signup(self, name: str, email: str):
        self.driver.find_element(*self.SIGNUP_NAME).send_keys(name)
        self.driver.find_element(*self.SIGNUP_EMAIL).send_keys(email)
        self.driver.find_element(*self.SIGNUP_BTN).click()

    def is_enter_account_information_visible(self) -> bool:
        return self.driver.find_element(*self.DETAILS_TXT).is_displayed()

    def is_login_error_visible(self) -> bool:
        return self.driver.find_element(*self.LOGIN_ERROR_TXT).is_displayed()

    def is_email_exists_error_visible(self) -> bool:
        return self.driver.find_element(*self.EMAIL_EXISTS_ERROR_TXT).is_displayed()