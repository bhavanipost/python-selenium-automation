from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
PARTICULAR_PRODUCT = (By.CSS_SELECTOR, ".a-section.aok-relative.s-image-fixed-height")
ADD_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button")
NO_PROTECTIONPLAN_BUTTON = (By.CSS_SELECTOR, '.a-button-input[aria-labelledby="attachSiNoCoverage-announce')
G0_TO_CART_BUTTON = (By.CSS_SELECTOR, "a[href='/cart?ref_=sw_gtc']")
SUB_TOTAL_BUTTON = (By.CSS_SELECTOR, "#sc-subtotal-label-buybox")


@when('search for treadmill')
def search_product(context):
    context.driver.find_element(*SEARCH_FIELD).send_keys('treadmill')
    context.driver.find_element(*SEARCH_BUTTON).click()

sleep(3)


@then('click on a particular product')
def particular_product_click(context):
    context.driver.find_element(*PARTICULAR_PRODUCT).click()


@then('Add to cart')
def add_cart(context):
    context.driver.find_element(*ADD_CART_BUTTON).click()
    context.driver.find_element(*NO_PROTECTIONPLAN_BUTTON).click()
    context.driver.find_element(*G0_TO_CART_BUTTON).click()
sleep(3)


@then('verify the added item in the cart')
def verify_added_item(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(*SUB_TOTAL_BUTTON).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

