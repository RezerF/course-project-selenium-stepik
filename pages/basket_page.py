from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert ('basket is empty' or 'корзина пуста') in empty_basket_text, 'Basket not empty'

    def is_not_good_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS_IN), \
            'Goods in basket, but should not be'