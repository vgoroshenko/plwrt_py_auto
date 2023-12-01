from pages.base.base_page import BasePage
from pages.locators import AddRemoveLocators
from playwright.sync_api import expect


class AddRemove(BasePage):
    def go_to_module(self):
        link = self.page.locator(AddRemoveLocators.ADD_REMOVE_PAGE)
        link.click()

    def should_be_add_remove_page_present(self):
        self.should_be_add_button_present()

    def should_be_add_button_present(self):
        expect(self.page.locator(AddRemoveLocators.ADD_BUTTON), 'should be Add button').to_be_visible()

    def should_be_remove_button_present(self):
        expect(self.page.locator(AddRemoveLocators.DELETE_BUTTON), 'should be Delete button').to_be_visible()

    def should_removed_element(self):
        expect(self.page.locator(AddRemoveLocators.DELETE_BUTTON), 'should not present Delete button').not_to_be_visible()

    def should_be_present_remove_buttons_count(self, num):
        buttons_count = self.page.locator(AddRemoveLocators.DELETE_BUTTON)
        expect(buttons_count, f'should be {num} buttons, but present {buttons_count}').to_have_count(num)

    def press_add_button_count(self, num):
        for _ in range(num):
            self.press_add_button()

    def press_add_button(self):
        button = self.page.locator(AddRemoveLocators.ADD_BUTTON)
        button.click()

    def press_delete_button(self):
        button = self.page.locator(AddRemoveLocators.DELETE_BUTTON).first
        button.click()

    def press_all_delete_buttons(self):
        self.click_all_elements(AddRemoveLocators.DELETE_BUTTON)

    def click_all_elements(self, selector):
        elements = self.page.query_selector_all(selector)
        for element in elements:
            element.click()
