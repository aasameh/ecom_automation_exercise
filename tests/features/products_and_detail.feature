Feature: Products and Product Detail

  Scenario: Verify All Products and product detail page
    Given I am on the home page
    When I click on 'Products' button
    Then user should be navigated to ALL PRODUCTS page successfully
    And the products list should be visible
    When I click on 'View Product' of first product
    Then user should be landed to product detail page
    And product details should be visible: product name, category, price, availability, condition, brand, image
