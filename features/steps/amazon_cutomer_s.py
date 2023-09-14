from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

CUSTOMER_SERVICE_PAGE = (By.CSS_SELECTOR,'a[href="/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice"]')
CHECK_HEADER = (By.CSS_SELECTOR, ".fs-heading.bolded[style='color: white;']")
UI_BOX = (By.CSS_SELECTOR, '.issue-card-container')
UI_ELEMENTS = (By.CSS_SELECTOR, '.issue-card-wrapper')
SEARCH_LIBRARY = (By.XPATH, "//h2[text()='Search our help library']")
CHECK_INPUTFIELD = (By.CSS_SELECTOR, '.a-input-text.a-span12')
ALL_HELP_TOPICS =  (By.XPATH, "//h2[text()='All help topics']")
HELP_TOPICS_LINK = (By.CSS_SELECTOR, '.help-topics')



@when('clicked on customer service')
def click_customer_service(context):
    context.driver.find_element(*CUSTOMER_SERVICE_PAGE).click()

@then('check for header is  visible')
def header_check(context):
    context.driver.find_element(*CHECK_HEADER)


@then ('check for UI elements')
def ui_element(context):
    context.driver.find_element(*UI_BOX)
   # context.driver.find_element(*UI_ELEMENTS)

@then('verify all {n2} UI elements')
def verify_link(context, n2):
    n2 = int(n2)
    link = context.driver.find_elements(*UI_ELEMENTS)
    assert len(link) == n2, f' Expected {n2} links but got {len(link)}'


@then('check for search help library')
def search_library(context):
    context.driver.find_element(*SEARCH_LIBRARY)


@then('check for input field for search library')
def search_inputfield(context):
    context.driver.find_element(*CHECK_INPUTFIELD)


@then('check for All help topics')
def all_help_topics(context):
    context.driver.find_element(*ALL_HELP_TOPICS)


@then('verify all {n3} links in All help topics')
def verify_link(context, n3):
    n3 = int(n3)
    all_link = context.driver.find_elements(*HELP_TOPICS_LINK)
    assert len(all_link) == n3, f' Expected {n3} links but got {len(all_link)}'



