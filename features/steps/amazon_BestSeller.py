
from behave import given, when, then
from selenium.webdriver.common.by import By

BEST_SELLER_PAGE = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
LINK_NUMBER = (By. CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR')



@when('click on Best Seller')
def click_best_seller(context):
    context.driver.find_element(*BEST_SELLER_PAGE).click()


@then('Verify that Best Seller has {n1}links')
def verify_link(context, n1):
    n1 = int(n1)
    links = context.driver.find_elements(*LINK_NUMBER)
    assert len(links) == n1, f' Expected {n1} links but got {len(links)}'

