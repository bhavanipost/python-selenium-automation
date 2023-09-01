# Created by bhavani at 8/22/23
Feature: Testing for the Sign in page when logged out user click orders

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Returns and Orders
    #Then Verify Sign in page is visible
    #Then Email input field is present

  # Enter feature description here

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify sign in page open


  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify Sign In is clickable
    When Wait for 3 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears
