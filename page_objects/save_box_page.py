from config import strings
from page_objects.base_page import BasePage

class SaveBox(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.save_box_url)
        self.browser.implicitly_wait(strings.timeout)

    def page_opened(self):
        text = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[7]/div/ul/li[7]/span[2]').text
        if text == 'Odkurzacz workowy ELECTROLUX EPF61RR':
            return True
        else:
            return False

    @property
    def cubby(self):
        return self.browser.find_elements_by_class('icons-schowek01')
    @property
    def cross(self):
        return self.browser.find_elements_by_class('mfp-close')

    def add_cubby(self):
        self.browser.execute_script("arguments[0].click();", self.cubby)
        info = self.browser.find_elements_by_class('m-typo m-typo_secondary').txt
        if info == "Produkt został dodany do schowka":
            return self.browser.execute_script("arguments[0].click();", self.cross) is True
        else:
            return False

    def sub_cubby(self):
        self.browser.execute_script("arguments[0].click();", self.cubby)
        info = self.browser.find_elements_by_class('m-typo m-typo_secondary').txt
        if info == "Produkt został usunięty ze schowka":
            return self.browser.execute_script("arguments[0].click();", self.cross) is True
        else:
            return False
