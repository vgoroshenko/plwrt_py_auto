from .base.base_page import BasePage
from .locators import DropdownLocators, BasePageLocators


class Dropdown(BasePage):

    def go_to_page(self):
        link = self.page.locator(DropdownLocators.DROPDOWN_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(BasePageLocators.PAGE_NAME)
        correct_text = 'Dropdown List'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def select_element_value(self, value):
        self.select_element_with_value(DropdownLocators.DROPDOWN_BUTTON, f'{value}')

    def should_be_selected_second(self):
        element = self.page.locator(DropdownLocators.DROPDOWN_SECOND_ELEMENT).get_attribute('selected')
        assert 'selected' in element.split()

    def should_be_selected_first(self):
        assert self.is_checked(DropdownLocators.DROPDOWN_FIRST_ELEMENT), 'should be selected first, but not'
