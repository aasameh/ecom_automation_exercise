from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .base_page import BasePage

class HomePage(BasePage):

    def click_home_btn(self): self.click(self.HOME_BTN)
    def click_signup_login_btn(self): self.click(self.SIGNUP_LOGIN_BTN)
    def click_products_btn(self): self.click(self.PRODUCTS_BTN)
    def click_cart_btn(self): self.click(self.CART_BTN)
    def click_test_cases_btn(self): self.click(self.TEST_CASES_BTN)
    def click_api_testing_btn(self): self.click(self.API_TESTING_BTN)
    def click_video_tut_btn(self): self.click(self.VIDEO_TUT_BTN)
    def click_contact_us_btn(self): self.click(self.CONTACT_US_BTN)
    def click_logout_btn(self): self.click(self.LOGOUT_BTN)
    def click_delete_account_btn(self): self.click(self.DELETE_ACCOUNT_BTN)
    def is_logged_in(self) -> bool:
        try: 
            return self.is_visible(self.LOGGED_IN_TXT).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False