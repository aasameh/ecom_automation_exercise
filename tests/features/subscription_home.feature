Feature: Subscription in Home Page

  Scenario: Verify Subscription in home page
    Given I am on the home page
    When I scroll down to footer
    Then text 'SUBSCRIPTION' should be visible
    When I enter email address in input and click arrow button
    Then success message 'You have been successfully subscribed!' should be visible
