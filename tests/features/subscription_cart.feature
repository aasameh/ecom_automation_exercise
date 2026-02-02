Feature: Subscription in Cart Page

  Scenario: Verify Subscription in Cart page
    Given I am on the home page
    When I click 'Cart' button
    And I scroll down to footer
    Then text 'SUBSCRIPTION' should be visible
    When I enter email address in input and click arrow button
    Then success message 'You have been successfully subscribed!' should be visible
