#Tomek
from page_objects.search_page import SearchPage

def correct_page(browser):
    search_page = SearchPage(browser)
    assert search_page.validate_logo_is_visible() is True
    assert search_page.validate_zalogujSie_is_visible() is True
    assert search_page.page_opened() is True

def test_6_1_search_monitor(browser):
    search_page = SearchPage(browser)
    assert search_page.correct_search() is True

def test_6_2_search_numbers(browser):
    search_page = SearchPage(browser)
    assert search_page.incorrect_search_1() is True

def test_6_3_search_word(browser):
    search_page = SearchPage(browser)
    assert search_page.incorrect_search_2() is True

def test_6_4_search_string(browser):
    search_page = SearchPage(browser)
    assert search_page.incorrect_search_3() is True
