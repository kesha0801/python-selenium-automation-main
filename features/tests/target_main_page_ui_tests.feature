Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open Target main page
    Then Verify header in shown

  Scenario: Verify 10 benefit cells
    Given Open Target main page
    When Get all benefit cells within circle
    Then Verify benefit cells has 10 links


  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header has 6 links
    Then Verify can click every link



# Homework 7 Scenario 1 below:

  Scenario: Verify user can access Signin
    Given Open target main page
    Then Click sign in button on header
    Then Click sign in button on side nav
    Then Verify sign in page is open




