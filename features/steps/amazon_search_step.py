from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('click on Returns and Orders')
def returns_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify Sign in page is visible')
def verify_signin_page(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then('Email input field is present')
def email_input(context):
    #expected_result = context.driver.find_element(By.XPATH, "//input[@type='email']").is_displayed()

    context.driver.find_element(By.CSS_SELECTOR, '#ap_email').is_displayed()







