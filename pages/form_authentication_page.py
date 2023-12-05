from pages.locators import FormAuthenticationLocators
from tests.test_data.test_data import TestData
from pages.base.base_page import BasePage


class FormAuthentication(BasePage):

    def click_login(self):
        button = self.page.locator(FormAuthenticationLocators.BUTTON_LOGIN)
        button.click()

    def click_logout(self):
        button = self.page.locator(FormAuthenticationLocators.BUTTON_LOGOUT)
        button.click()

    def click_close_message(self):
        button = self.page.locator(FormAuthenticationLocators.BUTTON_LOGOUT)
        button.click()

    def go_to_page(self):
        link = self.page.locator(FormAuthenticationLocators.LOADED_PAGE)
        link.click()

    def login(self):
        self.set_username()
        self.set_password()
        self.click_login()

    def set_username(self):
        user_field = self.page.locator(FormAuthenticationLocators.FIELD_USERNAME)
        user_field.type(TestData.USERS['user1']['username'])

    def set_password(self):
        password_field = self.page.locator(FormAuthenticationLocators.FIELD_PASSWORD)
        password_field.type(TestData.USERS['user1']['password'])

    def set_incorrect_password(self):
        password_field = self.page.locator(FormAuthenticationLocators.FIELD_PASSWORD)
        password_field.type('incorrect')

    def should_be_correct_page(self):
        text = self.get_text(FormAuthenticationLocators.PAGE_NAME)
        correct_text = 'Login Page'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_secure_area_page(self):
        text = self.get_text(FormAuthenticationLocators.PAGE_NAME)
        correct_text = 'Secure Area'
        assert correct_text in text, f'should be secure area page, but not'

    def should_be_success_login_message(self):
        text = self.get_text(FormAuthenticationLocators.SUCCESS_MESSAGE)
        correct_text = 'logged into'
        assert correct_text in text, f'should be success login message, but "{text}"'

    def should_be_success_logout_message(self):
        text = self.get_text(FormAuthenticationLocators.SUCCESS_MESSAGE)
        correct_text = 'logged out'
        assert correct_text in text, f'should be success logout message, but "{text}"'

    def should_be_failed_message(self):
        text = self.get_text(FormAuthenticationLocators.ERROR_MESSAGE)
        correct_text = 'is invalid'
        assert correct_text in text, f'should be error login message, but "{text}"'
