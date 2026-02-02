from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage

class ProductsPage(BasePage):
    PRODUCTS_LIST_TITLE = (By.XPATH, "//*[text()='All Products']")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    FIRST_PRODUCT_VIEW_BTN = (By.XPATH, "(//a[text()='View Product'])[1]")
    FIRST_PRODUCT_IMG = (By.XPATH, "(//div[@class='product-image-wrapper'])[1]")
    SEARCHED_PRODUCTS_TXT = (By.XPATH, "//*[text()='Searched Products']")

    def is_products_list_title_visible(self) -> bool:
        return self.driver.find_element(*self.PRODUCTS_LIST_TITLE).is_displayed()
    
    def is_first_product_img_visible(self) -> bool:
        return self.driver.find_element(*self.FIRST_PRODUCT_IMG).is_displayed()
        
    def search_product(self, query):
        self.send_keys(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BTN)
    
    def click_first_product_view_btn(self):
        self.driver.find_element(*self.FIRST_PRODUCT_VIEW_BTN).click()

    def are_searched_products_visible(self) -> bool:
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-image-wrapper']")
        return len(products) > 0

class ProductDetailPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    PRODUCT_CATEGORY = (By.XPATH, "//p[contains(text(), 'Category:')]")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']//span/span")
    PRODUCT_AVAILABILITY = (By.XPATH, "//p[b[text()='Availability:']]")
    PRODUCT_CONDITION = (By.XPATH, "//p[b[text()='Condition:']]")
    PRODUCT_BRAND = (By.XPATH, "//p[b[text()='Brand:']]")
    PRODUCT_IMG = (By.CSS_SELECTOR, ".view-product img")
    ADD_TO_CART_BTN = (By.XPATH, "//*[text()='Add to cart']")

    def are_product_details_visible(self, browser: WebDriver) -> bool:
        elements = {
            "Name": self.PRODUCT_NAME,
            "Category": self.PRODUCT_CATEGORY,
            "Price": self.PRODUCT_PRICE,
            "Availability": self.PRODUCT_AVAILABILITY,
            "Condition": self.PRODUCT_CONDITION,
            "Brand": self.PRODUCT_BRAND,
            "Image": self.PRODUCT_IMG,
        }
        
        for name, locator in elements.items():
            try:
                print(f"Checking {name}...")
                self.is_visible(locator)
            except Exception as e:
                print(f"{name} FAILED: {locator}")
                print(f"   Error: {e}")
                return False
        print("✅ All product details visible")
        return True

    def click_add_to_cart_btn(self):
        self.click(self.ADD_TO_CART_BTN)