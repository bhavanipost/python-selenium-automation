# Created by bhavani at 8/11/23
Feature: Test for Amazon product search
  # Enter feature description here
  Scenario Outline: Verify search result is correct
    Given Open Amazon page
    When Searching for <product>
    Then Verify <result> is correct
    Examples:
    |product      |result    |
    |spoon            |"spoon"          |
    |dress            |"dress"          |
