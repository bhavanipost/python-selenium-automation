
Feature: Test for every product name and image on Amazon search results page

  Scenario: Verify every product name and image on Amazon results page
    Given Open Amazon page
    When Searching for kettle
    Then Verify search result is "kettle"
    Then Verify every product name and image


