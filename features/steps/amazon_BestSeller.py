
from behave import given, when, then
from selenium.webdriver.common.by import By


TOP_MENU = (By.CSS_SELECTOR, 'div.celwidget.c-f ul a')
#BEST_SELLER_PAGE = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
#LINK_NUMBER = (By. CSS_SELECTOR, "#zg_header a")
#LINK_NUMBER = (By. CSS_SELECTOR, [class*="nav-tab"]  a')


@when('clicking on the Best Seller')
def click_best_seller(context):
    context.app.header.click_best_seller_btn()


@then('Verify that Best Seller has {n1} top menu')
def verify_link(context, n1):
    #n1 = int(n1)
    #links = context.driver.find_elements(*LINK_NUMBER)
    #assert len(links) == n1, f' Expected {n1} links but got {len(links)}'
    context.app.best_seller_page.verify_top_menu_count(n1)


@then('Verify each 5 top menu pages opens')
def verify_top_menu_page_opens(context):
    expected_text_top_menu = ['Amazon Best Sellers', 'Amazon Hot New Releases',
                              'Amazon Movers & Shakers', 'Amazon Most Wished For',
                              'Amazon Gift Ideas']
    actual_text_top_menu = []

    top_menu_links = context.driver.find_elements(*TOP_MENU)
    for menu_link in top_menu_links[:]:
        menu_link.click()
        current_top_menu = context.app.best_seller_page.get_text_top_menu()
        actual_text_top_menu.append(current_top_menu)
        return top_menu_links
    assert actual_text_top_menu == expected_text_top_menu, f'Expected {expected_text_top_menu} did not match actual {actual_text_top_menu}'
