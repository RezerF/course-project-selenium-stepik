from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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

