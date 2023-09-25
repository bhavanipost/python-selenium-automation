
Feature: Test for every product name and image on Amazon search results page

  Scenario: Verify every product name and image on Amazon results page
    Given Open Amazon page
    When Searching for kettle
    Then Verify search result is "kettle"
    Then Verify every product name and image

  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by alias <dept_name>
    When Searching for <product>
    Then Verify <search_dept> department is selected
    Examples:
    |dept_name    | product    |search_dept|
    |Handmade     |Handmade Jewelry  |Handmade  |
    |Books        | Medical books     |Books    |

