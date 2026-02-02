import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from typing import Generator
from pytest_bdd import given
import random
import os
import time

chrome_options = Options()

@pytest.fixture
def browser() -> Generator[WebDriver, None, None]:
    driver = webdriver.Chrome(options=chrome_options)

    # Offset window per worker
    worker = os.environ.get("PYTEST_XDIST_WORKER", "gw0")
    try: idx = int(worker.replace("gw", ""))
    except ValueError: idx = 0
    x = 50 + (idx * 40)
    y = 50 + (idx * 40)

    driver.set_window_position(x, y)
    driver.set_window_size(1200, 800)

    # Block common ad/track domains via CDP
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setBlockedURLs", {
        "urls": [
            "*://*.doubleclick.net/*",
            "*://*.g.doubleclick.net/*",
            "*://*.googleads.g.doubleclick.net/*",
            "*://*.googleadservices.com/*",
            "*://*.googlesyndication.com/*",
            "*://*.googletagservices.com/*",
            "*://*.adservice.google.com/*",
            "*://*.adsystem.com/*",
            "*://*.taboola.com/*",
            "*://*.outbrain.com/*",
            "*://*.adsrvr.org/*",
            "*://*.criteo.com/*"
        ]
    })
    driver.get("about:blank")
    time.sleep(2)
    driver.get("https://automationexercise.com/")
    assert "Automation Exercise" in driver.title
    yield driver
    driver.quit()

@pytest.fixture
def registered_account(browser: WebDriver):
    name = f"test{random.randint(1000, 9999)}"
    email = f"test{random.randint(1000, 9999)}@test.com"
    password = "testpassword"

    browser.find_element(By.XPATH, "//a[@href='/login']").click()
    assert browser.find_element(By.XPATH, "//*[contains(text(), 'New User Signup!')]").is_displayed()
    browser.find_element(By.CSS_SELECTOR, "[data-qa='signup-name']").send_keys(name)
    browser.find_element(By.CSS_SELECTOR, "[data-qa='signup-email']").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, "[data-qa='signup-button']").click()
    assert browser.find_element(By.XPATH, "//*[contains(text(), 'Enter Account Information')]").is_displayed()
    browser.find_element(By.CSS_SELECTOR, "[id='uniform-id_gender1']").click()
    browser.find_element(By.CSS_SELECTOR, "[id='password']").send_keys(password)
    Select(browser.find_element(By.CSS_SELECTOR, "[id='days']")).select_by_value("1")
    Select(browser.find_element(By.CSS_SELECTOR, "[id='months']")).select_by_value("1")
    Select(browser.find_element(By.CSS_SELECTOR, "[id='years']")).select_by_value("2001")
    browser.find_element(By.CSS_SELECTOR, "[id='newsletter']").click()
    browser.find_element(By.CSS_SELECTOR, "[id='optin']").click()
    browser.find_element(By.CSS_SELECTOR, "[id='first_name']").send_keys("first")
    browser.find_element(By.CSS_SELECTOR, "[id='last_name']").send_keys("last")
    browser.find_element(By.CSS_SELECTOR, "[id='company']").send_keys("company")
    browser.find_element(By.CSS_SELECTOR, "[id='address1']").send_keys("address1")
    browser.find_element(By.CSS_SELECTOR, "[id='address2']").send_keys("address2")
    Select(browser.find_element(By.CSS_SELECTOR, "[id='country']")).select_by_value("India")
    browser.find_element(By.CSS_SELECTOR, "[id='state']").send_keys("state")
    browser.find_element(By.CSS_SELECTOR, "[id='city']").send_keys("city")
    browser.find_element(By.CSS_SELECTOR, "[id='zipcode']").send_keys("zipcode")
    browser.find_element(By.CSS_SELECTOR, "[id='mobile_number']").send_keys("123456789")
    browser.find_element(By.CSS_SELECTOR, "[data-qa='create-account']").click()
    assert browser.find_element(By.XPATH, "//*[contains(text(), 'Account Created!')]").is_displayed()
    browser.find_element(By.CSS_SELECTOR, '[data-qa="continue-button"]').click()
    assert browser.find_element(By.XPATH, '//*[contains(text(), "Logged in as")]').is_displayed()
    browser.find_element(By.XPATH, "//a[@href='/logout']").click()
    
    yield {"name": name, "email": email, "password": password}
    
    # Cleanup: delete account
    try:
        browser.find_element(By.LINK_TEXT, 'Delete Account').click()
    except NoSuchElementException:
        browser.find_element(By.XPATH, "//a[@href='/login']").click()
        browser.find_element(By.CSS_SELECTOR, '[data-qa="login-email"]').send_keys(email)
        browser.find_element(By.CSS_SELECTOR, '[data-qa="login-password"]').send_keys(password)
        browser.find_element(By.CSS_SELECTOR, '[data-qa="login-button"]').click()

# Shared step for all tests
@given("I am on the home page")
def on_home_page(browser):
    """Browser fixture already navigates to home page and asserts title"""
    pass

