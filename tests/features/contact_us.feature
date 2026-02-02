Feature: Contact Us

  Scenario: Submit Contact Us form
    Given I am on the home page
    When I click on 'Contact Us' button
    Then 'GET IN TOUCH' should be visible
    When I enter name, email, subject and message
    And I upload a file
    And I click 'Submit' button
    And I click OK button
    Then success message 'Success! Your details have been submitted successfully.' should be visible
    When I click 'Home' button
    Then landed to home page successfully
