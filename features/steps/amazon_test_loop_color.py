from behave import given, when, then
from selenium.webdriver.common.by import By
#from time import sleep
from selenium.webdriver.support import expected_conditions as EC


#PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

#@when('Save product name')
#def get_product_name(context):
    #context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    #print(f'Current product: {context.product_name}')

@then('Verify user can select product colors by clicking through colors')
def verifying_can_click_colors(context):
    expected_colors = ['Black','Blue Over Dye','Dark Blue Vintage','Dark Indigo',
                       'Dark Wash','Indigo Wash','Light Wash','Medium Blue Vintage',
                       'Medium Wash','Rinsed','Vintage Wash','Washed Black','Bright White',
                       'Dark Khaki Brown','Light Khaki Brown','Olive','Light Blue Vintage',
                       'Washed Grey','Sage Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'



@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()

@then('Select one product hoodie')
def select_hoodie_product(context):
    context.app.header.select_hoodie_product()

@then('Verify that the user sees the deals')
def verify_user_see_deals(context):
    context.app.header.verify_user_see_deals()