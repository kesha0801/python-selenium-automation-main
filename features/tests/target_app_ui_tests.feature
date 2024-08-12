Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window


## Homework 8 Scenario below:

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    Then Click sign in button on header
    Then Click sign in button on side nav
    Given Store original window
    When Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page opened
    And Return to original window