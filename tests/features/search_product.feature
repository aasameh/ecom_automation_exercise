Feature: Search Product

  Scenario: Search for a product
    Given I am on the home page
    When I click on 'Products' button
    Then user should be navigated to ALL PRODUCTS page successfully
    When I enter product name in search input and click search button
    Then 'SEARCHED PRODUCTS' should be visible
    And all the products related to search should be visible
