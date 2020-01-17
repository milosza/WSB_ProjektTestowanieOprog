import logging
import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage

class AddressListPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.address_list_url)
        self.browser.implicitly_wait(strings.timeout)
        self._logger = logging.getLogger(__name__)

    @property
    def input_login_email(self):
        return self.browser.find_element_by_id("enp_customer_form_login_username")

    @property
    def input_login_password(self):
        return self.browser.find_element_by_id("enp_customer_form_login_password")

    @property
    def button_login(self):
        return self.browser.find_element_by_xpath('//*[@id="js-login"]/section/div/div[1]/div[2]/div[2]/form/div[4]/div/button')

    def page_opened(self):
        self.input_login_email.send_keys(strings.login_data["email"])
        self.input_login_password.send_keys(strings.login_data["password"])
        self.browser.execute_script("arguments[0].click();", self.button_login)
        time.sleep(strings.timeout)
        text = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div/ul/li[4]/span[2]').text
        if text == 'Książka adresowa':
            return True
        else:
            return False

    @property
    def button_new_address(self):
        return self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section[2]/div[1]/div[2]/a')

    @property
    def button_edit_address(self):
        return self.browser.find_element_by_xpath('//*[@id="address_7342382"]/div/div/div/div/div[2]/div[2]/a[1]')

    @property
    def input_address_name(self):
        return self.browser.find_element_by_id("enp_customer_form_type_address_relation_name")

    @property
    def input_email(self):
        return self.browser.find_element_by_id("enp_customer_form_type_address_relation_address_email")

    @property
    def input_email_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[5]/div[2]/em')

    @property
    def input_email_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[5]/div[2]/em')

    @property
    def radio_button_person(self):
        return self.browser.find_element_by_id(
            'enp_customer_form_type_address_relation_address_addressType_0')

    @property
    def input_firstname(self):
        return self.browser.find_element_by_id(
            "enp_customer_form_type_address_relation_address_firstName")

    @property
    def input_firstname_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[9]/div[2]/em')

    @property
    def input_firstname_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[9]/div[2]/em')

    @property
    def input_firstname_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[9]/div[2]/em')

    @property
    def input_lastname(self):
        return self.browser.find_element_by_id(
            "enp_customer_form_type_address_relation_address_lastName")

    @property
    def input_lastname_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[10]/div[2]/em')

    @property
    def input_lastname_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[10]/div[2]/em')

    @property
    def input_lastname_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[10]/div[2]/em')

    @property
    def input_street(self):
        return self.browser.find_element_by_id("enp_customer_form_type_address_relation_address_street")

    @property
    def input_street_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[11]/div[2]/em')

    @property
    def input_street_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[11]/div[2]/em')

    @property
    def input_street_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[11]/div[2]/em')

    @property
    def input_street_number(self):
        return self.browser.find_element_by_id(
            "enp_customer_form_type_address_relation_address_houseNumber")

    @property
    def input_street_number_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[12]/div[1]/div[2]/em')

    @property
    def input_street_number_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[12]/div[1]/div[2]/em')

    @property
    def input_zipcode(self):
        return self.browser.find_element_by_id(
            "enp_customer_form_type_address_relation_address_postcode")

    @property
    def input_zipcode_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[13]/div[2]/em')

    @property
    def input_zipcode_info_invalid(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[13]/div[2]/em')

    @property
    def input_city(self):
        return self.browser.find_element_by_id(
            "enp_customer_form_type_address_relation_address_city")

    @property
    def input_city_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[14]/div[2]/em')

    @property
    def input_city_info_short(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[14]/div[2]/em')

    @property
    def button_save_address(self):
        return self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/section[2]/div/div/form/div[16]/div[2]/input')

    @property
    def empty_field_prompts(self):
        return {self.input_firstname_info_empty.text: 'Podaj imię',
                self.input_lastname_info_empty.text: 'Podaj nazwisko',
                self.input_street_info_empty.text: 'Podaj ulicę',
                self.input_street_number_info_empty.text: 'Podaj numer domu',
                self.input_zipcode_info_empty.text: 'Podaj kod pocztowy',
                self.input_city_info_empty.text: 'Podaj nazwę miasta',
                }

    def empty_fields(self):
        try:
            print()
            print('Test 5.1.1')

            self.browser.execute_script("arguments[0].click();", self.button_new_address)
            self.browser.implicitly_wait(strings.timeout)
            self.input_address_name.clear()
            self.input_email.clear()
            self.input_firstname.clear()
            self.input_lastname.clear()
            self.input_street.clear()
            self.input_street_number.clear()
            self.input_zipcode.clear()
            self.input_city.clear()
            self.browser.execute_script("arguments[0].click();", self.button_save_address)

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
            pass

    def street_check(self):
        try:
            print()
            print('Test 5.1.2 - 5.1.3')

            self.browser.execute_script("arguments[0].click();", self.button_new_address)
            self.browser.implicitly_wait(strings.timeout)
            self.input_address_name.clear()
            self.input_email.clear()
            self.input_firstname.clear()
            self.input_lastname.clear()
            self.input_street.clear()
            self.input_street_number.clear()
            self.input_zipcode.clear()
            self.input_city.clear()
            self.browser.execute_script("arguments[0].click();", self.button_save_address)

            for entry in strings.address_data_invalid_street:
                self.input_street.send_keys(entry)
                print(entry , end=" ")
                if self.input_street_info_short.is_displayed() or self.input_street_info_invalid.is_displayed():
                    print('True')
                    self.input_street.clear()
                else:
                    print('Test failed, screenshot saved: street_check_'+str(strings.address_data_invalid_street.index(entry))+'.png')
                    self.browser.save_screenshot('street_check_'+str(strings.address_data_invalid_street.index(entry))+'.png')
                    return False
            return True
        except Exception as error:
            print(error)


    def street_number_check(self):
            print()
            print('Test 5.1.4')
            self.browser.execute_script("arguments[0].click();", self.button_new_address)
            self.browser.implicitly_wait(strings.timeout)
            self.input_address_name.clear()
            self.input_email.clear()
            self.input_firstname.clear()
            self.input_lastname.clear()
            self.input_street.clear()
            self.input_street_number.clear()
            self.input_zipcode.clear()
            self.input_city.clear()
            self.browser.execute_script("arguments[0].click();", self.button_save_address)

            for entry in strings.address_data_invalid_street_number:
                self.input_street_number.send_keys(entry)
                print(entry , end=" ")
                if self.input_street_number_info_invalid.is_displayed():
                    print('True')
                    self.input_street_number.clear()
                else:
                    print('Test failed, screenshot saved: street_number_check_'+str(strings.address_data_invalid_street_number.index(entry))+'.png')
                    self.browser.save_screenshot('street_number_check_'+str(strings.address_data_invalid_street_number.index(entry))+'.png')
                    return False
            return True

    def email_check(self):
            print()
            print('Test 5.1.5 - 5.1.9')
            self.browser.execute_script("arguments[0].click();", self.button_new_address)
            self.browser.implicitly_wait(strings.timeout)
            self.input_address_name.clear()
            self.input_email.clear()
            self.input_firstname.clear()
            self.input_lastname.clear()
            self.input_street.clear()
            self.input_street_number.clear()
            self.input_zipcode.clear()
            self.input_city.clear()
            self.browser.execute_script("arguments[0].click();", self.button_save_address)


            for entry in strings.address_data_invalid_email:
                self.input_email.send_keys(entry)
                self.browser.execute_script("arguments[0].click();", self.button_save_address)
                print(entry , end=" ")
                if self.input_email_info_short.is_displayed() or self.input_email_info_invalid.is_displayed():
                    print('True')
                    self.input_email.clear()
                else:
                    print('False')
                    return False
            return True

    def zipcode_check(self):
            print()
            print('Test 5.1.10')
            self.browser.execute_script("arguments[0].click();", self.button_new_address)
            self.browser.implicitly_wait(strings.timeout)
            self.input_address_name.clear()
            self.input_email.clear()
            self.input_firstname.clear()
            self.input_lastname.clear()
            self.input_street.clear()
            self.input_street_number.clear()
            self.input_zipcode.clear()
            self.input_city.clear()
            self.browser.execute_script("arguments[0].click();", self.button_save_address)

            for entry in strings.address_data_invalid_zipcode:
                self.input_zipcode.send_keys(entry)
                print(entry , end=" ")
                if self.input_zipcode_info_invalid.is_displayed():
                    print('True')
                    self.input_zipcode.clear()
                else:
                    print('False')
                    return False
            return True

    def new_address_save_check(self):
        print()
        print('Test 5.1.11')
        self.browser.execute_script("arguments[0].click();", self.button_new_address)
        self.browser.implicitly_wait(strings.timeout)
        self.input_address_name.clear()
        self.input_address_name.send_keys(strings.address_data["address_name"])
        self.input_email.clear()
        self.input_email.send_keys(strings.address_data["email"])
        self.input_firstname.clear()
        self.input_firstname.send_keys(strings.address_data["first_name"])
        self.input_lastname.clear()
        self.input_lastname.send_keys(strings.address_data["last_name"])
        self.input_street.clear()
        self.input_street.send_keys(strings.address_data["street"])
        self.input_street_number.clear()
        self.input_street_number.send_keys(strings.address_data["street_number"])
        self.input_zipcode.clear()
        self.input_zipcode.send_keys(strings.address_data["zipcode"])
        self.input_city.clear()
        self.input_city.send_keys(strings.address_data["city"])
        self.browser.execute_script("arguments[0].click();", self.button_save_address)
        time.sleep(strings.timeout)
        text_save_new_address_success = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
        print(text_save_new_address_success.text)
        if text_save_new_address_success.text == 'Nowy adres dodany':
            return True
        else:
            print('Test failed, screenshot saved: new_address_save_check.png')
            self.browser.save_screenshot('new_address_save_check_falied.png')
            return False

    def edit_address_no_change_check(self):
        print()
        print('Test 5.2.5')
        self.browser.execute_script("arguments[0].click();", self.button_edit_address)
        self.browser.implicitly_wait(strings.timeout)
        self.browser.execute_script("arguments[0].click();", self.button_save_address)
        time.sleep(strings.timeout)
        text_edited_address_no_change = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
        print(text_edited_address_no_change.text)
        if text_edited_address_no_change.text == 'Twoje dane nie zostały zmienione.':
            return True
        else:
            print('Test failed, screenshot saved: edited_address_no_change_check_fail.png')
            self.browser.save_screenshot('edited_address_no_change_check_fail.png')
            return False

    def edit_address_save_check(self):
        print()
        print('Test 5.2.6')
        self.browser.execute_script("arguments[0].click();", self.button_edit_address)
        self.browser.implicitly_wait(strings.timeout)

        self.input_street.clear()
        self.input_street.send_keys(strings.address_data["street"])
        self.input_street_number.clear()
        self.input_street_number.send_keys(strings.address_data["street_number"])

        self.browser.execute_script("arguments[0].click();", self.button_save_address)
        time.sleep(strings.timeout)
        text_save_edited_address_success = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
        print(text_save_edited_address_success.text)
        if text_save_edited_address_success.text == 'Twoje dane zostały zmienione.':
            return True
        else:
            print('Test failed, screenshot saved: edited_address_save_fail.png')
            self.browser.save_screenshot('edited_address_save_fail.png')
            return False
