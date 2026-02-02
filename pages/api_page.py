from selenium.webdriver.common.by import By
from .base_page import BasePage

class ApiPage(BasePage):
    """API Testing page - placeholder for future API test functionality"""
    API_LIST_TITLE = (By.XPATH, "//*[contains(text(), 'APIs List for practice')]")
    
    def is_api_page_visible(self) -> bool:
        try:
            return self.driver.find_element(*self.API_LIST_TITLE).is_displayed()
        except:
            return False
