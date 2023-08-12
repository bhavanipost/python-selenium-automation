from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Click on empty cart')
def click_empty_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]').click()

@then('Verify Amazon cart is empty')
def verify_cart_empty(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
