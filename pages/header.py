from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RETURN_ORDERS_ICON = (By.ID, 'nav-orders')
    SIGN_IN_PAGE_CHECK = (By.XPATH, "//h1[@class='a-spacing-small']")
    ER_EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    AR_EMAIL_INPUT = (By.CSS_SELECTOR, '#ap_email')


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def returns_orders(self):
        self.click(*self.RETURN_ORDERS_ICON)


    def verify_signin_text(self, expected_text):
        actual_text = self.find_element(*self.SIGN_IN_PAGE_CHECK).text
        assert actual_text == expected_text,  \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_email_input_field(self):
        expected_text = self.display(*self.ER_EMAIL_INPUT)
        actual_text = self.display(*self.AR_EMAIL_INPUT)
        assert actual_text == expected_text,  \
            f'Error, expected {expected_text} did not match actual {actual_text}'