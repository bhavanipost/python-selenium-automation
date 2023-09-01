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

@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    context.app.header.click_signin_from_popup()

@then('Verify Sign in page open')
def sign_in_page(context):
    context.app.sign_in_page.verify_signin_opened()


@then('Verify Sign In is clickable')
def verifying_signin_btn_clickable(context):
    context.app.header.verify_signin_btn_clickable()


@then('Verify Sign In disappears')
def verify_signin_btn_disappears(context):
    context.app.header.verify_signin_btn_disappears()





# #@then('Verify {text} page is visible')
# def verify_signin_page(context, text):
#     #expected_result = 'Sign in'
#     #actual_result = context.driver.find_element(*SIGN_IN_PAGE_CHECK).text
#
#     #assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     context.app.sign_in_page.verify_signin_opened(text)
#
# @then('Email input field is present')
# def email_field(context):
#     #expected_result = self.find_element(*ER_EMAIL_INPUT)
#     #actual_result = self.find_element(*AR_EMAIL_INPUT)
#     #assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     #context.driver.find_element(By.CSS_SELECTOR, '#ap_email').is_displayed()
#     context.app.sign_in_page.verify_email_input_field()






