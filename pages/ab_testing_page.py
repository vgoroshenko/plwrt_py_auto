from pages.base.base_page import BasePage
from pages.locators import ABPageLocators


class ABPage(BasePage):

    def go_to_ab_page(self):
        self.page.locator(ABPageLocators.AB_PAGE).click()

    def should_be_ab_page(self):
        text = 'No A/B Test'
        assert text in self.page.locator(
            ABPageLocators.NO_AB_TEXT).inner_text(), f'should be "No A/B Test", but "{text}"'
