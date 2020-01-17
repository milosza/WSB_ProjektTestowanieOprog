#Krystian
from page_objects.changing_password import ChangingPage
from page_objects.password_resetting import ResettingPage


def test_prerequisites_check_resetting_page_components(browser):
    password_resetting = ResettingPage(browser)
    assert password_resetting.validate_logo_is_visible() is True
    assert password_resetting.validate_zalogujSie_is_visible() is True
    assert password_resetting.page_opened() is True

def test_2_1_1_email_is_correct(browser):
    password_resetting = ResettingPage(browser)
    assert password_resetting.email_is_correct() is True

def test_2_1_2_email_is_wrong(browser):
    password_resetting = ResettingPage(browser)
    assert password_resetting.email_is_wrong() is True

def test_2_1_4_email_is_requied(browser):
    password_resetting = ResettingPage(browser)
    assert password_resetting.email_is_requied() is True

def test_prerequisites_check_changing_page_components(browser):
    changing_password = ChangingPage(browser)
    assert changing_password.validate_logo_is_visible() is True
    assert changing_password.validate_zalogujSie_is_visible() is True
    assert changing_password.page_opened() is True

def test_2_2_5_password_empty(browser):
    changing_password = ChangingPage(browser)
    assert changing_password.password_is_requied() is True

def test_2_2_4_one_password(browser):
    changing_password = ChangingPage(browser)
    assert changing_password.one_password() is True

def test_2_2_3_wrong_passwords(browser):
    changing_password = ChangingPage(browser)
    assert changing_password.wrong_passwords() is True

def test_2_2_2_password_is_correct(browser):
    changing_password = ChangingPage(browser)
    assert changing_password.password_is_correct() is True