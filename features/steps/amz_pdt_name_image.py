from behave import given, when, then
from selenium.webdriver.common.by import By
#
SEARCH_RESULT = (By.XPATH, '//span[@class ="a-color-state a-text-bold"]')
#PRODUCT_NAME = (By.CSS_SELECTOR, 'h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4')
PRODUCT_NAME = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
SEARCH_RESULTS = (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
PRODUCT_IMAGE = (By.CSS_SELECTOR, '.s-image[data-image-latency="s-product-image"]')
#PRODUCT_IMAGE = (By.CSS_SELECTOR, '.s-image')


@when('Select department by alias {dept}')
def select_dept(context, dept):
    context.app.header.select_dept(dept)


@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    #context.app.search_result_page.verify_search_result(expected_result)




@then('Verify every product name and image')
def verify_product_name_image(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        product_name = product.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert  product_name, 'Product name not shown'
        product.find_element(*PRODUCT_IMAGE)


@then('Verify {dept} department is selected')
def verify_dept_selected(context, dept):
        context.app.header.verity_dept_selected(dept)