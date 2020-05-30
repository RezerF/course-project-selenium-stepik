from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_in_product_page(self):
        self.add_to_cart(),
        self.should_be_correct_cost()
        self.should_be_good_in_cart(),
        self.should_not_be_success_message(),
        self.should_is_disappered()

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        link.click()

    def should_be_good_in_cart(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        substring = f"{name_book} has been added to your basket"
        assert substring in (self.browser.find_element(*ProductPageLocators.BOOK_CONFIRM_CART_TEXT)).text, \
            'Good not has been added to cart'

    def should_be_correct_cost(self):
        assert (self.browser.find_element(*ProductPageLocators.BOOK_CONFIRM_PRICE).text ==
                self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text), 'Price not correct'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_CONFIRM_CART_TEXT), \
            'Success message is presented, but should not be'

    def should_is_disappered(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_CONFIRM_CART_TEXT),\
            'Success message is not disappered.'
