@SwagLabs_cart
Feature: Adding an item to the cart

  Scenario: Add an item to the shopping cart
    Given I am on the SwagLabs homepage
    When I click on the first item
    And I add it to the cart
    And I click on cart icon
    Then I should see the item in the shopping cart



