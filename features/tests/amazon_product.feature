# Created by bhavani at 8/1/23
Feature:User check added item in cart

  Scenario: Check for added item in cart
    Given Open Amazon page
    When search for treadmill
    Then click on a particular product
    Then Add to cart
    Then verify the added item in the cart
