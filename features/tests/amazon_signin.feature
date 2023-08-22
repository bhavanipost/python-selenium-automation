# Created by bhavani at 8/22/23
Feature: Testing for the Sign in page when logged out user click orders

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Returns and Orders
    Then Verify Sign in page is visible
    Then Email input field is present
  # Enter feature description here

