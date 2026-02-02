from pytest_bdd import scenarios, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from pages.products_page import ProductsPage, ProductDetailPage

scenarios('../features/products_and_detail.feature')

@when("I click on 'Products' button")
def click_products_button(browser: WebDriver):
    ProductsPage(browser).click(ProductsPage(browser).PRODUCTS_BTN)
    
@then("user should be navigated to ALL PRODUCTS page successfully")
def on_products_page(browser: WebDriver):
    assert "/products" in browser.current_url

@then("the products list should be visible")
def product_list_visible(browser:WebDriver):
    assert ProductsPage(browser).is_products_list_title_visible()
    assert ProductsPage(browser).is_first_product_img_visible()

@when("I click on 'View Product' of first product")
def click_view_product(browser:WebDriver):
    ProductsPage(browser).click(ProductsPage(browser).FIRST_PRODUCT_VIEW_BTN)

@then("user should be landed to product detail page")
def on_details_page(browser: WebDriver):
    assert "/product_details" in browser.current_url

@then("product details should be visible: product name, category, price, availability, condition, brand, image")
def product_details_visible(browser: WebDriver):
    assert ProductDetailPage(browser).are_product_details_visible(browser)