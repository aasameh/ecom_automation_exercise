from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:

    # Navbar locators
    LOGO_HOME_BTN = (By.CSS_SELECTOR, "#header .logo a")
    HOME_BTN = (By.LINK_TEXT, " Home")
    PRODUCTS_BTN = (By.XPATH, "//*[@href='/products']")
    CART_BTN = (By.XPATH, "//*[@href='/view_cart']")
    SIGNUP_LOGIN_BTN = (By.XPATH, "//*[@href='/login']")
    TEST_CASES_BTN = (By.XPATH, "//*[@href='/test_cases']")
    API_TESTING_BTN = (By.XPATH, "//*[@href='/api_list']")
    VIDEO_TUT_BTN = (By.LINK_TEXT, " Video Tutorials")
    CONTACT_US_BTN = (By.XPATH, "//*[@href='/contact_us']")
    LOGOUT_BTN = (By.XPATH, "//*[@href='/logout']")
    DELETE_ACCOUNT_BTN = (By.XPATH, "//*[@href='/delete_account']")
    LOGGED_IN_TXT = (By.XPATH, "//*[contains(text(), 'Logged in as')]")


    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def get_text(self, locator):
        return self.is_visible(locator).text
    
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