# Created by bhavani at 8/1/23
Feature:User check added item in cart

  Scenario: Check for added item in cart
    Given Open Amazon page
    When search for treadmill
    Then click on a particular product
    When wait for 3 sec
    Then Add to cart
    When wait for 3 sec
    Then verify the Subtotal (1 item): in the cart
