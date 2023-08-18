# Created by bhavani at 8/10/23
Feature: Test for Best Seller to verify 5 links
  # Enter feature description here

  Scenario: Verify that Best Seller has 5 links
    Given Open Amazon page
    When click on Best Seller
    Then Verify that Best Seller has 5 links
