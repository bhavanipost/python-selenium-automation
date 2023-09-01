# Created by bhavani at 8/10/23
Feature: Test for Best Seller to verify 5 links
  # Enter feature description here

  Scenario: Verify that Best Seller has 5 top menu
    Given Open Amazon page
    When clicking on the Best Seller
    Then Verify that Best Seller has 5 top menu
    Then Verify each 5 top menu pages opens