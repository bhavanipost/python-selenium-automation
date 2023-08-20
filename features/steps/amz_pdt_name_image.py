# from behave import given, when, then
# from selenium.webdriver.common.by import By
# #
# #
# PRODUCT_NAME = (By.CSS_SELECTOR, 'h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4')
# SEARCH_RESULTS = (By.CSS_SELECTOR, 'div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20')
# PRODUCT_IMAGE = (By.CSS_SELECTOR, '.s-image[data-image-latency="s-product-image"]')
# #PRODUCT_IMAGE = (By.CSS_SELECTOR, '.s-image')74
#

# @then('Verify every product name and image')
# def verify_product_name_image(context):
#     all_products = context.driver_find_elements(*SEARCH_RESULTS)

    # for product in all_products:
    #     product_name = product.find_element(*PRODUCT_NAME).text
    #     print(product_name)
    #     assert  product_name, 'Print title not shown'
    #     product.find_element(*PRODUCT_IMAGE)