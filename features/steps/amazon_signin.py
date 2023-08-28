from behave import given, when, then
from selenium.webdriver.common.by import By
RETURN_ORDERS_ICON = (By.ID, 'nav-orders')
SIGN_IN_PAGE_CHECK = (By.XPATH, "//h1[@class='a-spacing-small']")
ER_EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
#AR_EMAIL_INPUT = (By.CSS_SELECTOR, '#ap_email')
AR_EMAIL_INPUT = (By.ID, 'ap_email')
@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('click on Returns and Orders')
def returns_orders(context):
    #context.driver.find_element(*RETURN_ORDERS_ICON).click()
    context.app.header.returns_orders()


@then('Verify {text} page is visible')
def verify_signin_page(context, text):
    #expected_result = 'Sign in'
    #actual_result = context.driver.find_element(*SIGN_IN_PAGE_CHECK).text

    #assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.header.verify_signin_text(text)

@then('Email input field is present')
def email_field(context):
    #expected_result = context.driver.find_element(*ER_EMAIL_INPUT).is_displayed()
    #actual_result = context.driver.find_element(*AR_EMAIL_INPUT).is_displayed()
    #assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    #context.driver.find_element(By.CSS_SELECTOR, '#ap_email').is_displayed()
    context.app.header.verify_email_input_field()






