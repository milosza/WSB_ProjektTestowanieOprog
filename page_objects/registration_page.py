import logging
import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class RegistrationPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.registration_url)
        self.browser.implicitly_wait(strings.timeout)
        self._logger = logging.getLogger(__name__)

    def page_opened(self):
        text = self.browser.find_element_by_xpath('//*[@id="js-register"]/section/div/div/form/div/div[2]/div/p').text
        if text == 'Załóż konto':
            return True
        else:
            return False

    @property
    def radio_button_mrs(self):
        return self.browser.find_element_by_id(
            'js-salutation_misses')

    @property
    def radio_button_mr(self):
        return self.browser.find_element_by_id(
            'js-salutation_mister')
    @property
    def radio_button_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[5]/div/label[2]/em')

    @property
    def input_firstname(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_firstName")

    @property
    def input_firstname_info_empty(self):
        return self.browser.find_element_by_xpath(
            '// *[@id="js-register"]/section/div/div/form/div/div[2]/div/div[6]/div[2]/em')

    @property
    def input_firstname_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[6]/div[2]/em')

    @property
    def input_firstname_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[6]/div[2]/em')

    @property
    def input_lastname(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_lastName")

    @property
    def input_lastname_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[7]/div[2]/em')

    @property
    def input_lastname_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[7]/div[2]/em')

    @property
    def input_lastname_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[7]/div[2]/em')

    @property
    def input_email(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_email")

    @property
    def input_email_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[10]/div[2]/em')

    @property
    def input_email_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[10]/div[2]/em')

    @property
    def input_email_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[10]/div[2]/em')

    @property
    def input_password(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_plainPassword")

    @property
    def input_password_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[11]/div[2]/em')

    @property
    def input_password_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[11]/div[2]/em')

    @property
    def input_phone(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_mobileNumber_number")

    @property
    def input_phone_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[12]/div[2]/em')

    @property
    def input_phone_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[12]/div[2]/em')

    @property
    def input_zipcode(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_postcode")

    @property
    def input_zipcode_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[16]/div[2]/em')

    @property
    def input_zipcode_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[16]/div[2]/em')

    @property
    def checkbox_terms_and_conditions(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_consentForm_consent_686_0")

    @property
    def checkbox_terms_and_conditions_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-checkboxes"]/label[1]/label/em')

    @property
    def button_save(self):
        return self.browser.find_element_by_xpath('//*[@id="js-checkboxesRegister"]/div[1]/div[2]/div[2]/button')

    @property
    def empty_field_prompts(self):
        return {self.radio_button_info_empty.text: 'Wybierz zwrot',
                self.input_firstname_info_empty.text: 'Podaj imię',
                self.input_lastname_info_empty.text: 'Podaj nazwisko',
                self.input_email_info_empty.text: 'Podaj adres email',
                self.input_password_info_empty.text: 'Podaj hasło',
                self.input_phone_info_empty.text: 'Podaj numer telefonu',
                self.input_zipcode_info_empty.text: 'Podaj kod pocztowy',
                self.checkbox_terms_and_conditions_info_empty.text: 'To pole jest wymagane'
                }

    def empty_fields(self):
        try:
            print()
            print('Test 1.1.1')

            self.browser.execute_script("arguments[0].click();", self.button_save)
            self.browser.implicitly_wait(strings.timeout)

            for field in self.empty_field_prompts:
                print(field, '=', self.empty_field_prompts[field], '?', end=" ")
                if field == self.empty_field_prompts[field]:
                    print('True')
                else:
                    print('False')
                    self.browser.save_screenshot('empty_fields_false.png')
                    return False
            return True
        except Exception as error:
            print(error)

    def firstname_check(self):
            print()
            print('Test 1.1.2 - 1.1.3')
            self.browser.execute_script("arguments[0].click();", self.button_save)
            self.browser.implicitly_wait(strings.timeout)
            for entry in strings.registration_data_invalid_firstname:
                self.input_firstname.send_keys(entry)
                print(entry , end=" ")
                if self.input_firstname_info_short.is_displayed() or self.input_firstname_info_invalid.is_displayed():
                    print('True')
                    self.input_firstname.clear()
                else:
                    print('False')
                    return False
            return True

    def lastname_check(self):
            print()
            print('Test 1.1.4 - 1.1.5')
            self.browser.execute_script("arguments[0].click();", self.button_save)
            self.browser.implicitly_wait(strings.timeout)
            for entry in strings.registration_data_invalid_lastname:
                self.input_lastname.send_keys(entry)
                print(entry , end=" ")
                if self.input_lastname_info_short.is_displayed() or self.input_lastname_info_invalid.is_displayed():
                    print('True')
                    self.input_lastname.clear()
                else:
                    print('False')
                    return False
            return True

    def email_check(self):
            print()
            print('Test 1.1.6 - 1.1.9')
            self.browser.execute_script("arguments[0].click();", self.button_save)
            self.browser.implicitly_wait(strings.timeout)
            for entry in strings.registration_data_invalid_email:
                self.input_email.send_keys(entry)
                print(entry , end=" ")
                if self.input_email_info_short.is_displayed() or self.input_email_info_invalid.is_displayed():
                    print('True')
                    self.input_email.clear()
                else:
                    print('False')
                    return False
            return True

    def password_check(self):
            print()
            print('Test 1.1.10')
            self.browser.execute_script("arguments[0].click();", self.button_save)
            self.browser.implicitly_wait(strings.timeout)
            for entry in strings.registration_data_invalid_password:
                self.input_password.send_keys(entry)
                print(entry , end=" ")
                if self.input_password_info_short.is_displayed():
                    print('True')
                    self.input_password.clear()
                else:
                    print('False')
                    return False
            return True

    def phone_check(self):
            print()
            print('Test 1.1.11')
            self.browser.execute_script("arguments[0].click();", self.button_save)
            self.browser.implicitly_wait(strings.timeout)
            for entry in strings.registration_data_invalid_phone:
                self.input_phone.send_keys(entry)
                print(entry , end=" ")
                if self.input_phone_info_invalid.is_displayed():
                    print('True')
                    self.input_phone.clear()
                else:
                    print('False')
                    return False
            return True

    def zipcode_check(self):
            print()
            print('Test 1.1.12')
            self.browser.execute_script("arguments[0].click();", self.button_save)
            self.browser.implicitly_wait(strings.timeout)
            for entry in strings.registration_data_invalid_zipcode:
                self.input_zipcode.send_keys(entry)
                print(entry , end=" ")
                if self.input_zipcode_info_invalid.is_displayed():
                    print('True')
                    self.input_zipcode.clear()
                else:
                    print('False')
                    return False
            return True

    def db_data_exists(self):
        try:
            print()
            print('Test 1.2.1 - 1.2.2')

            self.browser.execute_script("arguments[0].click();", self.radio_button_mr)
            self.input_firstname.send_keys(strings.registration_data["first_name"])
            self.input_lastname.send_keys(strings.registration_data["last_name"])
            self.input_email.send_keys(strings.registration_data["email"])
            self.input_password.send_keys(strings.registration_data["password"])
            self.input_phone.send_keys(strings.registration_data["phone"])
            self.input_zipcode.send_keys(strings.registration_data["zipcode"])
            self.browser.execute_script("arguments[0].click();", self.checkbox_terms_and_conditions)
            self.browser.execute_script("arguments[0].click();", self.button_save)
            #self.browser.implicitly_wait(strings.timeout)
            time.sleep(strings.timeout)

            text_phone = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
            text_email = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[4]/div')

            fields = {text_phone.text: 'Podany numer telefonu istnieje już w bazie',
                      text_email.text: 'Email '+strings.registration_data["email"]+' jest zajęty'
                      }

            for field in fields:
                print(field, '=', fields[field], '?', end=" ")
                if field == fields[field]:
                    print('True')
                else:
                    print('False')
                    self.browser.save_screenshot('db_data_exists_false.png')
                    return False
            return True
        except Exception as error:
            print(error)
            print('False')
            self.browser.save_screenshot('db_data_exists_false.png')

