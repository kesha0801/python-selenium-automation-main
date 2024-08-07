Feature: Target main page search tests


  Scenario: User can search for fan
    Given Open target main page
    When Search for fan
    Then Verify search results shown for fan
    Then Verify correct search results URL opens for fan

  # Make sure scenario names are unique:

  Scenario: User can search for a pen
    Given Open target main page
    When Search for pen
    Then Verify search results shown for pen
    Then Verify correct search results URL opens for pen

  Scenario: User can search for an table
    Given Open target main page
    When Search for table
    Then Verify search results shown for table
    And Verify correct search results URL opens for table

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <expected_result>
    And Verify correct search results URL opens for <expected_result>
    Examples:
    |product  |expected_result    |
    |fan      |fan                |
    |pen      |pen                |
    |table    |table              |


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image