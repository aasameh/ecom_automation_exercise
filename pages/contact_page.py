from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class ContactPage(BasePage):
    GET_IN_TOUCH_TXT = (By.XPATH, "//*[contains(text(), 'Get In Touch')]")
    CONTACT_NAME =  (By.NAME, "name")
    CONTACT_EMAIL = (By.NAME, "email")
    CONTACT_SUBJECT = (By.NAME, "subject")
    CONTACT_MESSAGE = (By.NAME, "message")
    CONTACT_FILE_UPLOAD = (By.NAME, "upload_file")
    CONTACT_SUBMIT_BTN = (By.NAME, "submit")
    CONTACT_SUCCESS_MSG = (By.XPATH, "//*[contains(text(), 'Success! Your details have been submitted successfully.')]")
    CONTACT_HOME_BTN = (By.CSS_SELECTOR, '.btn-success i')

    def enter_contact_details(self, name: str, email:str, subject:str, message:str):
        self.send_keys(self.CONTACT_NAME, name)
        self.send_keys(self.CONTACT_EMAIL, email)
        self.send_keys(self.CONTACT_SUBJECT, subject)
        self.send_keys(self.CONTACT_MESSAGE, message)
    def upload_file(self, file_path: str):
        self.send_keys(self.CONTACT_FILE_UPLOAD, file_path)