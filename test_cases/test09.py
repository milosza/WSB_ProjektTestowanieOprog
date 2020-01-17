#Tomek
from page_objects.login_page import LoginPage
from page_objects.bonus_code_page import BonusCode

def test_logger(logger):
    logger.info("Logowanie z poziomu testów")

def test_9_1_add_correct_promotion_code(browser):
    bonus_code = BonusCode(browser)
    assert bonus_code.promotion_items() is True

