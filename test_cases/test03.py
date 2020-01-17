#Tomek
from page_objects.login_page import LoginPage

def correct_login_page(browser):
    login_page = LoginPage(browser)
    assert login_page.validate_logo_is_visible() is True
    assert login_page.validate_zalogujSie_is_visible() is True
    assert login_page.page_opened() is True

def test_3_1_1_correct_data(browser):
    login_page = LoginPage(browser)
    assert login_page.login() is True

def test_3_1_2_incorrect_email(browser):
    login_page = LoginPage(browser)
    assert login_page.login_1() is True

def test_3_1_3_incorrect_syntax_email(browser):
    login_page = LoginPage(browser)
    assert login_page.login_2() is True

def test_3_1_4_incorrect_password(browser):
    login_page = LoginPage(browser)
    assert login_page.login_3() is True

def test_3_1_5_incorrect_syntax_password(browser):
    login_page = LoginPage(browser)
    assert login_page.login_4() is True

def test_3_2_1_correct_account(browser):
    login_page = LoginPage(browser)
    assert login_page.login_google_account() is True

def test_3_2_2_incorrect_account(browser):
    login_page = LoginPage(browser)
    assert login_page.login_google_account() is False
