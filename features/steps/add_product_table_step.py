from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_NAME = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
NAME_ITEM = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@when('Searching for {an_item}')
def item_search(context, an_item):
    context.driver.find_element(*SEARCH_NAME).send_keys(an_item)
    context.driver.find_element(*SEARCH_BTN).click()


@then('Verify {expected_result} is correct')
def verify_search(context,expected_result):
    item_name = context.driver.find_element(*NAME_ITEM).text
    assert expected_result == item_name, f'Error,expected{expected_result} did not match actual {item_name}'