Feature: Login functionality

  Scenario: Login with valid credentials
    Given the user navigates to the login page
    When the user enters valid credentials
    Then the user should be logged in and see the welcome message

  Scenario: Failed login with invalid credentials
    Given the user navigates to the login page
    When the user enters invalid credentials
    Then the user should see an error message



