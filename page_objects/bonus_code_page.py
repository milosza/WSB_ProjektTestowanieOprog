from config import strings
from page_objects.base_page import BasePage

class BonusCode(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.discount_url)
        self.browser.implicitly_wait(strings.timeout)

    @property
    def discount_code(self):
        self.browser.find_elements_by_class_name('js-discountCode_toggleTrigger')

    @property
    def promo_coupon(self):
        self.browser.find_elements_by_id('cart_flow_type_promo_coupon')

    @property
    def promo_button(self):
        self.browser.find_elements_by_id('js-promo-submit')

    @property
    def discount(self):
        self.browser.find_elements_by_class("m-cartSummary_price")


    def promotion_items(self):
        self.browser.execute_script("arguments[0].click();", self.discount_code)
        self.browser.input_inner.send_key(strings.discount_data('a'))
        final_price = self.browser.find_elements_by_class('m-cartSummary_price')
        price = self.browser.find_elements_by_class('m-cartSummary_price')
        if final_price == price:
            return False
        else:
            return True
