# Created by bhavani at 9/10/23
Feature: Tests for 404 page
  # Enter feature description here

    Scenario Outline: User is able to navigate to amazon blog from 404 page
        Given Open Amazon product <product_id> page
        And Store original window
        When Clicking on a dog image
        And Switch to new window
        Then Verify blog is opened
        And Close blog
        And Return to original window
        Examples:
            | product_id        |
            | B07NF5WGQ11111111 |

