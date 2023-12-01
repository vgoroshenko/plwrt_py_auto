from pages.base.base_page import BasePage
from .locators import BasicAuthLocators


class BasicAuth(BasePage):

    def go_to_module(self):
        self.page.goto(f'http://admin:admin@{self.url[7:]}basic_auth')

    def go_to_failed_module(self):
        self.page.goto(f'http://admin:admin1@{self.url[7:]}basic_auth')

    def should_be_success_basic_auth_page(self):
        text = self.page.locator(BasicAuthLocators.CONGRAT_MESSAGE)
        self.expect(text, f'should be Congratulations, but present {text.inner_text()}').to_contain_text('Congratulations!')
        #assert 'Congratulations!' in text, f'should be Congratulations, but present {text}'

    def should_be_present_failed_message(self):
        text = self.page.locator(BasicAuthLocators.FAILED_MESSAGE)
        self.expect(text, f'should be Not authorized, but present {text.inner_text()}').to_contain_text('')
        #assert '' in text, f'should be Not authorized, but present {text}'
