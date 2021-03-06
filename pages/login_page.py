from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.current_url
        assert "login" in login_link, 'Link not correct'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), 'Login form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTRATION), 'Registration form is not present'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_FORM)\
            .send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASS_REGISTRATION_FORM)\
            .send_keys(password)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.PASS_CONFIRM_REGISTRATION_FORM)\
            .send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()


