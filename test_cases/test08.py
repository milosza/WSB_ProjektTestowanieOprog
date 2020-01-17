#Miłosz
from page_objects.product_page import ProductPage

def test_logger(logger):
    logger.info("Logowanie z poziomu testów")

def test_prerequisites_check_product_page_components(browser):
    product_page = ProductPage(browser)
    assert product_page.validate_logo_is_visible() is not None
    assert product_page.validate_zalogujSie_is_visible() is not None
    assert product_page.page_opened() is not None

def test_8_1_1_to_8_1_3_product_avaibility_city_validation(browser):
    product_page = ProductPage(browser)
    assert product_page.city_check() is not None