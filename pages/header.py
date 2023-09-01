from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RETURN_ORDERS_ICON = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    #SIGN_IN_PAGE_CHECK = (By.XPATH, "//h1[@class='a-spacing-small']")
    #ER_EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    #AR_EMAIL_INPUT = (By.CSS_SELECTOR, '#ap_email')
    #AR_EMAIL_INPUT = (By.ID, 'ap_email')
    GOTO_CART_ICON = (By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]')
    PARTICULAR_PRODUCT = (By.CSS_SELECTOR, ".a-section.aok-relative.s-image-fixed-height")
    BEST_SELLER_BTN = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


    def click_product(self):
         self.click(*self.PARTICULAR_PRODUCT)


    def returns_orders(self):
        self.click(*self.RETURN_ORDERS_ICON)


    def click_cart_icon(self):
        self.click(*self.GOTO_CART_ICON)


    def click_best_seller_btn(self):
        self.click(*self.BEST_SELLER_BTN)

    # def verify_signin_text(self, expected_text):
    #     actual_text = self.find_element(*self.SIGN_IN_PAGE_CHECK).text
    #     assert actual_text == expected_text,  \
    #         f'Error, expected {expected_text} did not match actual {actual_text}'

    #def verify_email_input_field(self):
        #expected_text = self.display(*self.ER_EMAIL_INPUT)
        #actual_text = self.display(*self.AR_EMAIL_INPUT)
        #assert actual_text == expected_text,  \
            #f'Error, expected {expected_text} did not match actual {actual_text}'
        #self.find_element(*self.AR_EMAIL_INPUT)



    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(*self.SIGNIN_BTN)

    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(*self.SIGNIN_BTN)
