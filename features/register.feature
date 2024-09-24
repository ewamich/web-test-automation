Feature: User Registration

  Scenario: Successful registration
    Given the user navigates to the registration page
    When the user enters valid registration details
    Then the user should see a confirmation message

  Scenario: Registration with existing email
    Given the user navigates to the registration page
    When the user enters an email that’s already registered
    Then the user should see an error message about duplicated email