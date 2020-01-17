import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class BucketPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.bucket_product_url)
        self.browser.implicitly_wait(strings.timeout)

    def page_opened(self):
        text = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[7]/div[1]/div[2]/h1').text
        if text == 'Telewizor SAMSUNG UE65RU7452U':
            return True
        else:
            return False

    @property
    def button_buy_now(self):
        return self.browser.find_element_by_xpath('//*[@id="js-offerBar"]/div/div[4]/a')

    @property
    def button_save(self):
        return self.browser.find_element_by_xpath('//*[@id="js-postcode-submit"]')

    @property
    def button_go_to_bucket(self):
        return self.browser.find_element_by_xpath('//*[@id="js-preCartNext"]')

    @property
    def button_add(self):
        return self.browser.find_element_by_xpath('//*[@id="js-cart-list-form"]/div[2]/table/tbody/tr[1]/td[5]/div/div/span[1]')

    @property
    def button_remove(self):
        return self.browser.find_element_by_xpath('//*[@id="js-cart-list-form"]/div[2]/table/tbody/tr[1]/td[5]/div/div/span[2]')

    @property
    def input_post_code(self):
        return self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/div/div/form/div/div[1]/div/input")

    def product_add_no_log_empty_post(self):
        self.browser.execute_script("arguments[0].click();", self.button_buy_now)
        self.browser.implicitly_wait(strings.timeout)
        self.browser.execute_script("arguments[0].click();", self.button_save)
        self.browser.implicitly_wait(strings.timeout)
        text_error = self.browser.find_element_by_xpath('//*[@id="js-preCart"]/div[1]/div/div/div')
        time.sleep(10)
        if text_error.text == 'Nie znaleziono kodu pocztowego':
            self.browser.delete_all_cookies()
            return True
        else:
            return False

    def product_add_no_log_wrong_post(self):
        self.browser.execute_script("arguments[0].click();", self.button_buy_now)
        self.browser.implicitly_wait(strings.timeout)
        self.input_post_code.send_keys(strings.bucket_data["post_code_wrong"])
        self.browser.execute_script("arguments[0].click();", self.button_save)
        self.browser.implicitly_wait(strings.timeout)
        text_error = self.browser.find_element_by_xpath('//*[@id="js-preCart"]/div[1]/div/div/div')
        time.sleep(10)
        if text_error.text == 'Nie znaleziono kodu pocztowego':
            self.browser.delete_all_cookies()
            return True
        else:
            return False

    def product_add_no_log_correct_post(self):
        self.browser.execute_script("arguments[0].click();", self.button_buy_now)
        self.browser.implicitly_wait(strings.timeout)
        self.input_post_code.send_keys(strings.bucket_data["post_code"])
        self.browser.execute_script("arguments[0].click();", self.button_save)
        self.browser.implicitly_wait(strings.timeout)
        time.sleep(10)
        text_error = self.browser.find_element_by_xpath('//*[@id="js-preCart"]/p')
        time.sleep(10)
        if text_error.text == 'Dodałeś pomyślnie produkt do koszyka':
            self.browser.delete_all_cookies()
            return True
        else:
            return False

    def product_add_from_bucket(self):
        self.browser.execute_script("arguments[0].click();", self.button_buy_now)
        self.browser.implicitly_wait(strings.timeout)
        self.input_post_code.send_keys(strings.bucket_data["post_code"])
        self.browser.execute_script("arguments[0].click();", self.button_save)
        self.browser.implicitly_wait(strings.timeout)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_go_to_bucket)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_go_to_bucket)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_add)
        time.sleep(10)
        text_sum = self.browser.find_element_by_xpath('//*[@id="js-cart-list-form"]/div[2]/table/tbody/tr[1]/td[4]/p')
        text_delivery = self.browser.find_element_by_xpath('//*[@id="js-cart-list-content"]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[2]/span')
        text_all = self.browser.find_element_by_xpath('//*[@id="js-cartTotal"]/td[2]/span')
        if (int(text_sum.text.replace(' zł', '').replace(' ', '').replace(',', ''))* 2) ++ int(text_delivery.text.replace(' zł', '').replace(' ', '').replace(',', '')) == int(text_all.text.replace(' zł', '').replace(' ', '').replace(',', '')) :
            self.browser.delete_all_cookies()
            return True
        else:
            return False

    def product_add_delivery(self):
        self.browser.execute_script("arguments[0].click();", self.button_buy_now)
        self.browser.implicitly_wait(strings.timeout)
        self.input_post_code.send_keys(strings.bucket_data["post_code"])
        self.browser.execute_script("arguments[0].click();", self.button_save)
        self.browser.implicitly_wait(strings.timeout)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_go_to_bucket)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_go_to_bucket)
        time.sleep(10)
        text_sum = self.browser.find_element_by_xpath('//*[@id="js-cart-list-content"]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/span')
        text_delivery = self.browser.find_element_by_xpath('//*[@id="js-cart-list-content"]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[2]/span')
        text_all = self.browser.find_element_by_xpath('//*[@id="js-cartTotal"]/td[2]/span')
        if int(text_sum.text.replace(' zł', '').replace(' ', '').replace(',', ''))++ int(text_delivery.text.replace(' zł', '').replace(' ', '').replace(',', '')) == int(text_all.text.replace(' zł', '').replace(' ', '').replace(',', '')) :
            self.browser.delete_all_cookies()
            return True
        else:
            return False

    def product_remove_from_bucket(self):
        self.browser.execute_script("arguments[0].click();", self.button_buy_now)
        self.browser.implicitly_wait(strings.timeout)
        self.input_post_code.send_keys(strings.bucket_data["post_code"])
        self.browser.execute_script("arguments[0].click();", self.button_save)
        self.browser.implicitly_wait(strings.timeout)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_go_to_bucket)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_go_to_bucket)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_add)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_remove)
        time.sleep(10)
        text_price = self.browser.find_element_by_xpath('//*[@id="js-cart-list-form"]/div[2]/table/tbody/tr[1]/td[4]/p')
        text_sum = self.browser.find_element_by_xpath('//*[@id="js-cart-list-content"]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/span')
        if text_price.text == text_sum.text:
            self.browser.delete_all_cookies()
            return True
        else:
            return False

    def product_remove_all_from_bucket(self):
        self.browser.execute_script("arguments[0].click();", self.button_buy_now)
        self.browser.implicitly_wait(strings.timeout)
        self.input_post_code.send_keys(strings.bucket_data["post_code"])
        self.browser.execute_script("arguments[0].click();", self.button_save)
        self.browser.implicitly_wait(strings.timeout)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_go_to_bucket)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_go_to_bucket)
        time.sleep(10)
        self.browser.execute_script("arguments[0].click();", self.button_remove)
        time.sleep(10)
        text_error = self.browser.find_element_by_xpath('//*[@id="js-cart-list-content"]/div[2]/div[1]/p')
        if text_error.text == 'Twój koszyk jest pusty.':
            self.browser.delete_all_cookies()
            return True
        else:
            return False
