Feature: User Login

  Scenario: Login with correct email and password
    Given I am on the home page
    Given I am a registered user
    When I click on 'Signup / Login' button
    Then 'Login to your account' should be visible
    When I enter correct email address and password
    And I click 'login' button
    Then 'Logged in as username' should be visible