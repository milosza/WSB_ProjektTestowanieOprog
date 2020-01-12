import logging
import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class ProductPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.product_url)
        self.browser.implicitly_wait(strings.timeout)
        self._logger = logging.getLogger(__name__)

    def page_opened(self):
        pricebox = self.browser.find_element_by_xpath('//*[@id="js-rightContent"]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]')
        if pricebox.is_displayed():
            return True
        else:
            return False

    @property
    def button_where_to_buy(self):
        return self.browser.find_element_by_xpath('//*[@id="js-availability"]/ul/li[4]/span[2]/span')

    @property
    def button_search_city(self):
        return self.browser.find_element_by_xpath('//*[@id="availability"]/div/div/div/div[3]/div[2]/button')

    @property
    def search_city_info_empty(self):
        return self.browser.find_element_by_xpath('//*[@id="availability"]/ul/li')

    @property
    def search_city_info_invalid(self):
        return self.browser.find_element_by_xpath('//*[@id="availability"]/ul/li')

    @property
    def button_add_to_cart(self):
        return self.browser.find_element_by_xpath('//*[@id="availability"]/ul/li[1]/div[2]/div[2]/ul/div/a')

    @property
    def input_city(self):
        return self.browser.find_element_by_id('city')

    def city_check(self):
        try:
            print()
            print('Test 8.1.1 - 8.1.3')

            self.browser.execute_script("arguments[0].click();", self.button_where_to_buy)
            self.browser.implicitly_wait(strings.timeout)

            for entry in strings.product_availability_cities_list:
                self.input_city.send_keys(entry)
                self.browser.execute_script("arguments[0].click();", self.button_search_city)
                self.browser.implicitly_wait(strings.timeout)
                print(entry, end=" ")
                if self.search_city_info_empty.is_displayed() or self.search_city_info_invalid.is_displayed() or self.button_add_to_cart.is_displayed():
                    print('True')
                    self.input_city.clear()
                else:
                    print('Test failed, screenshot saved: product_availability_city_check_' + str(strings.product_availability_cities_list.index(entry)) + '.png')
                    self.browser.save_screenshot(
                        'product_availability_city_check_' + str(strings.product_availability_cities_list.index(entry)) + '.png')
                    return False
            return True
        except Exception as error:
            print(error)