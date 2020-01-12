from page_objects.registration_page import RegistrationPage
from page_objects.login_page import LoginPage

def test_logger(logger):
    logger.info("Logowanie z poziomu testów")

def test_prerequisites_check_registration_page_components(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.validate_logo_is_visible()
    assert registration_page.validate_zalogujSie_is_visible()
    assert registration_page.page_opened()

def test_1_1_1_create_account_empty_fields_validation(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.empty_fields()

def test_1_1_2_to_1_1_3_create_account_firstname_validation(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.firstname_check()

def test_1_1_4_to_1_1_5_create_account_lastname_validation(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.lastname_check()

def test_1_1_6_to_1_1_9_create_account_email_validation(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.email_check()

def test_1_1_10_create_account_password_validation(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.password_check()

def test_1_1_11_create_account_phone_and_zipcode_validation(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.phone_check()
    assert registration_page.zipcode_check()

def test_1_2_1_to_1_2_2_create_account_customer_already_exists(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.db_data_exists()

def test_1_4_1_first_login(browser):
    login_page = LoginPage(browser)
    assert login_page.login() is True

# def test_1_1_create_account_field_validation(browser):
#     registration_page = RegistrationPage(browser)
#     assert registration_page.empty_fields()
#     assert registration_page.firstname_check()
#     assert registration_page.lastname_check()
#     assert registration_page.email_check()
#     assert registration_page.password_check()
#     assert registration_page.phone_check()
#     assert registration_page.zipcode_check()