from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

#@when('Click on search')
#def search_item(context):
    #context.driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").click()
#sleep(3)

@when('search for treadmill')
def search_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('treadmill')


@then('click on search')
def product_click(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

sleep(3)



@then('click on a particular product')
def particular_product_click(context):
    context.driver.find_element(By.CSS_SELECTOR, ".a-section.aok-relative.s-image-fixed-height").click()

@then('Add to cart')
def add_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()
    context.driver.find_element(By.CSS_SELECTOR, '.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]').click()
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart?ref_=sw_gtc']").click()
sleep(3)

@then('verify the added item in the cart')
def added_item(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#sc-subtotal-label-buybox").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

