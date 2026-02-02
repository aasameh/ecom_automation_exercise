from pytest_bdd import scenarios, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from pages.products_page import ProductsPage, ProductDetailPage

scenarios('../features/search_product.feature')

@when("I click on 'Products' button")
def click_products_button(browser: WebDriver):
    ProductsPage(browser).click(ProductsPage(browser).PRODUCTS_BTN)

@then("user should be navigated to ALL PRODUCTS page successfully")
def on_products_page(browser: WebDriver):
    assert '/products' in browser.current_url

@when("I enter product name in search input and click search button")
def search_product(browser: WebDriver):
    ProductsPage(browser).search_product("Blue")

@then("'SEARCHED PRODUCTS' should be visible")
def is_searched_products_visible(browser: WebDriver):
    assert ProductsPage(browser).is_visible(ProductsPage(browser).SEARCHED_PRODUCTS_TXT)

@then("all the products related to search should be visible")
def are_searched_products_visible(browser: WebDriver):
    assert ProductsPage(browser).are_searched_products_visible()