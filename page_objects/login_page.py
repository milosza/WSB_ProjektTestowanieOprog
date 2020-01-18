from config import strings
from page_objects.base_page import BasePage
import time

class LoginPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.login_url)
        self.browser.implicitly_wait(strings.timeout)

    def page_opened(self):
        text = self.browser.find_element_by_class('m-typo m-typo_primary').text
        if text == 'Zaloguj się przez':
            return True
        else:
            return False

    @property
    def input_email(self):
        return self.browser.find_element_by_id("enp_customer_form_login_username")

    @property
    def input_password(self):
        return self.browser.find_element_by_id("enp_customer_form_login_password")

    @property
    def button_login(self):
        return self.browser.find_element_by_xpath('//*[@id="js-login"]/section/div/div[1]/div[2]/div[2]/form/div[4]/div/button')

    @property
    def button_log_out(self):
        return self.browser.find_element_by_xpath('//*[@id="js-accountInfo"]/span[3]/a')

    @property
    def login_by_google_account(self):
        return self.browser.find_element_by_class("m-btn is-google")

    @property
    def choice_google_account(self):
        return self.browser.find_element_by_jsname("bQIQze")

    def login(self):
        self.input_email.send_keys(strings.login_data["email"])
        self.input_password.send_keys(strings.login_data["password"])
        self.browser.execute_script("arguments[0].click();", self.button_login)
        # self.browser.implicitly_wait(strings.timeout)
        time.sleep(strings.timeout)
        icon = self.browser.find_element_by_xpath('//*[@id="js-accountInfo"]/span/a')
        log_out = self.browser.find_element_by_xpath('//*[@id="js-accountInfo"]/span[3]/a')
        if icon != log_out:
            self.browser.execute_script("arguments[0].click();", self.button_log_out)
            return True
        else:
            return False

    def login_1(self):
        self.input_email.send_keys(strings.login_data["email1"])
        self.input_password.send_keys(strings.login_data["password"])
        self.browser.execute_script("arguments[0].click();", self.button_login)
        # self.browser.implicitly_wait(strings.timeout)
        time.sleep(strings.timeout)
        inccorect_data = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
        return inccorect_data.text

    def login_2(self):
        self.input_email.send_keys(strings.login_data["email2"])
        self.input_password.send_keys(strings.login_data["password"])
        self.browser.execute_script("arguments[0].click();", self.button_login)
        # self.browser.implicitly_wait(strings.timeout)
        time.sleep(strings.timeout)

        inccorect_data = self.browser.find_element_by_xpath(
            '//*[@id="js-login"]/section/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/em')
        return inccorect_data.text

    def login_3(self):
        self.input_email.send_keys(strings.login_data["email"])
        self.input_password.send_keys(strings.login_data["password1"])
        self.browser.execute_script("arguments[0].click();", self.button_login)
        # self.browser.implicitly_wait(strings.timeout)
        time.sleep(strings.timeout)
        inccorect_data = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
        return inccorect_data.text

    def login_4(self):
        self.input_email.send_keys(strings.login_data["email"])
        self.input_password.send_keys(strings.login_data["password2"])
        self.browser.execute_script("arguments[0].click();", self.button_login)
        # self.browser.implicitly_wait(strings.timeout)
        time.sleep(strings.timeout)
        inccorect_data = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
        return inccorect_data.text

    def login_google_account(self):
        self.browser.execute_script("arguments[0].click();", self.login_by_google_account)
        self.browser.execute_script("arguments[0].click();", self.choice_google_account)