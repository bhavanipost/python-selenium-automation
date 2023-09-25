# Created by bhavani at 8/16/23
Feature:Test for colors through loop and verify choice of color is displayed when clicked
  # Enter feature description here

#  Scenario: Verify user can select the product colors by clicking the colors
#    Given Open Amazon product B07BJKRR25 page
#    Then Verify user can select product colors by clicking through colors

Scenario Outline: Select a product from Closing category and hover over New Arrivals
    Given Open Amazon page
    When Searching for <product>
    Then Select one product hoodie
    When Hover over New Arrivals
    Then Verify that the user sees the deals
    Examples:
      | product            |
      | hoodie for girls |