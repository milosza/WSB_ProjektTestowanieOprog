#Miłosz
from page_objects.login_page import LoginPage
from page_objects.address_list_page import AddressListPage

def test_logger(logger):
    logger.info("Logowanie z poziomu testów")

def test_prerequisites_check_address_list_page_components(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.validate_logo_is_visible() is not None
    assert address_list_page.validate_zalogujSie_is_visible() is not None
    assert address_list_page.page_opened() is not None

def test_5_1_1_new_address_empty_fields_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.empty_fields()

def test_5_1_2_to_5_1_3_new_address_street_check_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.street_check()

def test_5_1_4_new_address_street_number_check_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.street_number_check()

def test_5_1_5_to_5_1_9_new_address_email_check_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.email_check()

def test_5_1_10_new_address_zipcode_check_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.zipcode_check()

def test_5_1_11_new_address_save_success_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.new_address_save_check()

def test_5_2_5_edited_address_no_change_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.page_opened()
    assert address_list_page.edit_address_no_change_check()

def test_5_2_6_edited_address_save_success_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.edit_address_save_check()
