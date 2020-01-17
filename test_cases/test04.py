#Krystian
from page_objects.bucket_checking import BucketPage

def test_prerequisites_check_resetting_page_components(browser):
    bucket_checking = BucketPage(browser)
    assert bucket_checking.validate_logo_is_visible() is True
    assert bucket_checking.validate_zalogujSie_is_visible() is True
    assert bucket_checking.page_opened() is True

def test_4_2_add_delivery(browser):
    bucket_checking = BucketPage(browser)
    assert bucket_checking.product_add_delivery() is True

def test_4_3_3_add_product(browser):
    bucket_checking = BucketPage(browser)
    assert bucket_checking.product_add_from_bucket() is True

def test_4_4_2_remove_one_product(browser):
    bucket_checking = BucketPage(browser)
    assert bucket_checking.product_remove_from_bucket() is True

def test_4_4_3_remove_all_product(browser):
    bucket_checking = BucketPage(browser)
    assert bucket_checking.product_remove_all_from_bucket() is True

def test_4_1_3_wrong_post_code(browser):
    bucket_checking = BucketPage(browser)
    assert bucket_checking.product_add_no_log_wrong_post() is True

def test_4_1_4_empty_post_code(browser):
    bucket_checking = BucketPage(browser)
    assert bucket_checking.product_add_no_log_empty_post() is True

def test_4_1_2_correct_post_code(browser):
    bucket_checking = BucketPage(browser)
    assert bucket_checking.product_add_no_log_correct_post() is True