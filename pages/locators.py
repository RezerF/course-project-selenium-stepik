from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, '#login_form')
    FORM_REGISTRATION = (By.CSS_SELECTOR, '#register_form')
    EMAIL_ENTER_FORM = (By.CSS_SELECTOR, "#id_login-username")
    PASS_ENTER_FORM = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_ENTER_FORM = (By.CSS_SELECTOR, '[name = "login_submit"]')
    EMAIL_REGISTRATION_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    PASS_REGISTRATION_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    PASS_REPEATED_REGISTRATION_FORM = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE_BOOK = (By.CSS_SELECTOR, '.product_main > p')
    NAME_BOOK = (By.CSS_SELECTOR, '.product_main > h1')
    NAME_BOOK_CONFIRM_CART = (By.XPATH, '//div[@class="alertinner "]/strong')
    BOOK_CONFIRM_CART_TEXT = (By.XPATH, '//div[@class="alertinner "]')
    BOOK_CONFIRM_PRICE = (By.XPATH, '//div[@class="alertinner "]/p/strong')

