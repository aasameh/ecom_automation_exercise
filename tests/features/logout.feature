Feature: User Logout

  Scenario: Logout after login
    Given I am on the home page
    When I click on 'Signup / Login' button
    Then 'Login to your account' should be visible
    When I enter correct email address and password
    And I click 'login' button
    Then 'Logged in as username' should be visible
    When I click 'Logout' button
    Then user should be navigated to login page
