from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import time, pytest

#@pytest.mark.parametrize('promo',[
#'?promo=offer0',
#'?promo=offer1',
#'?promo=offer2',
#'?promo=offer3',
#'?promo=offer4',
#'?promo=offer5',
#'?promo=offer6',
# pytest.param('?promo=offer7', marks=pytest.mark.xfail),
#'?promo=offer8',
#'?promo=offer9'
#])
#def test_guest_can_add_product_to_basket(browser, promo):
#    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_cart()
#    page.solve_quiz_and_get_code()
#    page.should_be_good_in_cart()
#    page.should_be_correct_cost()
#
#@pytest.mark.xfail(reason='Fixed right now')
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8'
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_cart()
#    page.solve_quiz_and_get_code()
#    page.should_not_be_success_message()
#
#def test_guest_cant_see_success_message(browser):
#    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8'
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_not_be_success_message()
#
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_empty_basket()
    page_basket.is_not_good_in_basket()

#@pytest.mark.xfail(reason='Fixed right now')
#def test_message_disappeared_after_adding_product_to_basket(browser):
#    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8'
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_cart()
#    page.solve_quiz_and_get_code()
#    page.should_is_disappered()
#
#def test_guest_should_see_login_link_on_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_be_login_link()
#
#def test_guest_can_go_to_login_page_from_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.go_to_login_page()
#

