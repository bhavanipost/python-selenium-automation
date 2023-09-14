# Created by bhavani at 8/1/23
Feature:User check added item in cart

  Scenario Outline: Check for added item in cart
    Given Open Amazon page
    When search for treadmill
    Then clicking on a particular product
    When wait for 3 sec
    Then Add product to cart
    When wait for 3 sec
    Then verify the <added_item> in the cart
    Examples:
      | added_item         |
      | Subtotal (1 item): |
