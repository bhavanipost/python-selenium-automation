# Created by bhavani at 8/1/23
Feature:Testing on empty Amazon cart

  Scenario:User search on Amazon cart is empty
    Given Open Amazon page
    When Click on empty cart
    Then Verify cart text Your Amazon Cart is empty
