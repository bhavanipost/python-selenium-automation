# Created by bhavani at 8/11/23
Feature: Test for UI elements in Customer servive page


  Scenario: Verify UI elements are present in the customer service  page
    Given Open Amazon page
    When click on customer service
    Then check for header is  visible
    Then check for UI elements
    Then verify all 11 UI elements
    Then check for search help library
    Then check for input field for search library
    Then check for All help topics
    Then verify all 12 links in All help topics
