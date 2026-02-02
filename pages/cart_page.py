from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Cart elements
    CART_ITEMS = (By.CSS_SELECTOR, "[id='cart_items']")
    
    # Footer - Subscription (same as home page)
    SUBSCRIPTION_TXT = (By.XPATH, "//*[text()='Subscription']")
    SUBSCRIPTION_EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIPTION_ARROW_BTN = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS_MSG = (By.XPATH, "//*[contains(text(), 'You have been successfully subscribed!')]")
    
    def scroll_to_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def is_subscription_visible(self) -> bool:
        return self.driver.find_element(*self.SUBSCRIPTION_TXT).is_displayed()
    
    def subscribe_with_email(self, email: str):
        self.driver.find_element(*self.SUBSCRIPTION_EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.SUBSCRIPTION_ARROW_BTN).click()
    
    def is_subscription_success_visible(self) -> bool:
        return self.driver.find_element(*self.SUBSCRIPTION_SUCCESS_MSG).is_displayed()
