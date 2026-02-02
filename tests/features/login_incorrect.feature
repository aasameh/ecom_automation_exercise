Feature: User Login

  Scenario: Login with incorrect email and password
    Given I am on the home page
    When I click on 'Signup / Login' button
    Then 'Login to your account' should be visible
    When I enter incorrect email address and password
    And I click 'login' button
    Then error 'Your email or password is incorrect!' should be visible