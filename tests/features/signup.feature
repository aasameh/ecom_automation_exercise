Feature: User Signup and Account Deletion
Scenario: Register, Login, and delete account successfully

Given I am on the home page
When I click on 'Signup / Login' button
Then 'New User Signup!' should be visible
When I sign up
Then 'ENTER ACCOUNT INFORMATION' should be visible
When I fill details: Title, Password, Date of birth
And I Select checkbox 'Sign up for our newsletter!'
And I Select checkbox 'Receive special offers from our partners!'
And I Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
And I Click 'Create Account button'
Then 'ACCOUNT CREATED!' should be visible
When I Click 'Continue' button
Then 'Logged in as username' should be visible
When I Click 'Delete Account' button
Then 'ACCOUNT DELETED!' should be visible
Then I Click 'Continue' button