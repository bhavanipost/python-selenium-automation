from behave import given, when, then
from selenium.webdriver.common.by import By

# PRODUCT_NAME = (By.CSS_SELECTOR, '.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4')
#
#
# PRODUCT_IMAGE = (By.CSS_SELECTOR, 'div.a-section.aok-relative.s-image-square-aspect img.s-image')
#
#
# #@then('Verify every product name and image')
# #def verify_pdt_name_image(context):
#     #context.product_name = context.driver.find_element(*PRODUCT_NAME).text
#     #print(f'Current product: {context.product_name}')
#
# @then('Verify every product name and image')
# def verify_product_name_image(context):
#
#     prdt_name = []
#     prdt_img = []
#
#     name = context.driver.find_elements(*PRODUCT_NAME)
#     for n2 in name[:10]:
#          n3 = context.driver_find_elements(*PRODUCT_NAME).text