#Tomek
import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class SearchPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.home_url)
        self.browser.implicitly_wait(strings.timeout)

    @property
    def input_search(self):
        return self.browser.find_element_by_class('m-search_inputInner is-active')

    @property
    def icon_search(self):
        return self.browser.find_element_by_id('beheader-search')

    def correct_search(self):
        self.input_search.send_key(strings.search_data['a'])
        self.browser.execute_script("arguments[0].click();", self.icon_search)
        self.browser.implicitly_wait(strings.timeout)
        category = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[4]/h1')
        if category.txt == "Monitory ":
            return True
        else:
            return False

    def incorrect_search_1(self):
        self.browser.input_inner.send_key(strings.search_data("b"))
        self.browser.execute_script("arguments[0].click();", self.icon_search)
        article_title = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[4]/section/article/header/h1/text()[2]')
        if article_title == "Niestety nie udało się znaleźć wyszukiwanego produktu.":
            return True
        else:
            return False

    def incorrect_search_2(self):
        self.browser.input_inner.send_key(strings.search_data("c"))
        self.browser.execute_script("arguments[0].click();", self.icon_search)
        article_title = self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/div[4]/section/article/header/h1/text()[2]')
        if article_title == "Niestety nie udało się znaleźć wyszukiwanego produktu.":
            return True
        else:
            return False

    def incorrect_search_3(self):
        self.browser.input_inner.send_key(strings.search_data("d"))
        self.browser.execute_script("arguments[0].click();", self.icon_search)
        article_title = self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/div[4]/section/article/header/h1/text()[2]')
        if article_title == "Niestety nie udało się znaleźć wyszukiwanego produktu.":
            return True
        else:
            return False

