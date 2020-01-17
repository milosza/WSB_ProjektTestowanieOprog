import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class ResettingPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.resetting_url)
        self.browser.implicitly_wait(strings.timeout)

    def page_opened(self):
        text = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[1]/p').text
        if text == 'Zmiana hasła (Krok 1 z 2)':
            return True
        else:
            return False

    @property
    def button_generate(self):
        return self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[2]/div/form/div[2]/input')

    @property
    def input_email(self):
        return self.browser.find_element_by_id(
            "email")

    def email_is_requied(self):
        self.browser.execute_script("arguments[0].click();", self.button_generate)
        self.browser.implicitly_wait(strings.timeout)
        text_email = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[2]/div/form/div[1]/div[2]/em')
        time.sleep(10)
        if text_email.text == 'E-mail jest wymagany':
            return True
        else:
            return False

    def email_is_wrong(self):
        self.input_email.send_keys(strings.resetting_data["email2"])
        self.browser.execute_script("arguments[0].click();", self.button_generate)
        self.browser.implicitly_wait(strings.timeout)
        text_email = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[2]/div/form/div[1]/div[2]/em')
        time.sleep(10)
        if text_email.text == 'Nieprawidłowy adres email':
            return True
        else:
            return False

    def email_is_correct(self):
        self.input_email.send_keys(strings.resetting_data["email"])
        self.browser.execute_script("arguments[0].click();", self.button_generate)
        self.browser.implicitly_wait(strings.timeout)
        text_email = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[1]/p')
        time.sleep(10)
        if text_email.text == 'Jeśli podany w formularzu adres email jest poprawny i powiązany z Twoim kontem klienta, wysłaliśmy na niego email umożliwiający odzyskanie hasła.' or text_email.text == 'W przeciągu ostatnich 12 godzin nastąpiła już próba odzyskania hasła.':
            return True
        else:
            return False
