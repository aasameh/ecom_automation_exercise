Feature: User Registration

  Scenario: Register with existing email
    Given I am on the home page
    When I click on 'Signup / Login' button
    Then 'New User Signup!' should be visible
    When I enter name and already registered email address
    And I click 'Signup' button
    Then error 'Email Address already exist!' should be visible
