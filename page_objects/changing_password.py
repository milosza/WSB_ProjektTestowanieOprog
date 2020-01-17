import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class ChangingPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.changing_password_url)
        self.browser.implicitly_wait(strings.timeout)

    def page_opened(self):
        text = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[1]/p').text
        if text == 'Zmiana hasła (Krok 2 z 2)':
            return True
        else:
            return False

    @property
    def button_generate(self):
        return self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[2]/div/form/div[3]/button')

    @property
    def input_password_1(self):
        return self.browser.find_element_by_id(
            "fos_user_resetting_form_plainPassword_first")

    @property
    def input_password_2(self):
        return self.browser.find_element_by_id(
            "fos_user_resetting_form_plainPassword_second")

    def password_is_requied(self):
        self.browser.execute_script("arguments[0].click();", self.button_generate)
        self.browser.implicitly_wait(strings.timeout)
        text_password_1 = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[2]/div/form/div[1]/div[2]/em')
        text_password_2 = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[2]/div/form/div[2]/div[2]/em')
        time.sleep(10)
        if text_password_1.text == 'Podaj hasło' and text_password_2.text == 'Podaj hasło':
            return True
        else:
            return False

    def one_password(self):
        self.input_password_1.send_keys(strings.changing_password_data["password"])
        self.browser.execute_script("arguments[0].click();", self.button_generate)
        self.browser.implicitly_wait(strings.timeout)
        text_password_1 = self.browser.find_element_by_xpath('//*[@id="pwindicator"]/div[2]')
        text_password_2 = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[2]/div/form/div[2]/div[2]/em')
        time.sleep(10)
        if text_password_1.text != 'Podaj hasło' and text_password_2.text == 'Podaj hasło':
            return True
        else:
            return False

    def wrong_passwords(self):
        self.input_password_1.send_keys(strings.changing_password_data["password"])
        self.input_password_2.send_keys(strings.changing_password_data["wrong_password"])
        self.browser.execute_script("arguments[0].click();", self.button_generate)
        self.browser.implicitly_wait(strings.timeout)
        text_password_1 = self.browser.find_element_by_xpath('//*[@id="pwindicator"]/div[2]')
        text_password_2 = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section/div/div/div[2]/div[2]/div/form/div[2]/div[2]/em')
        time.sleep(10)
        if text_password_1.text != 'Podaj hasło' and text_password_2.text == 'Podaj hasło takie same jak powyżej':
            return True
        else:
            return False

    def password_is_correct(self):
        self.input_password_1.send_keys(strings.changing_password_data["password"])
        self.input_password_2.send_keys(strings.changing_password_data["password"])
        self.browser.execute_script("arguments[0].click();", self.button_generate)
        self.browser.implicitly_wait(strings.timeout)
        text_correct = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
        time.sleep(10)
        if text_correct.text == 'Hasło zostało zresetowane':
            return True
        else:
            return False
