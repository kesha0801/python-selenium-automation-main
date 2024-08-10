Feature: Tests for Cart functionality



  #Homework 7 updating below scenario to page object pattern

  Scenario: Product is added to cart
    Given Open target main page
    When Search for pencil
    Then Click add to cart
    Then Verify cart has correct product



  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown



