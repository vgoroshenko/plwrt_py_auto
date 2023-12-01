from pages.locators import ChallengingDomLocators
from pages.base.base_page import BasePage


class ChallengingDom(BasePage):

    def go_to_page(self):
        link = self.page.locator(ChallengingDomLocators.CHALLENGING_DOM_PAGE)
        link.click()

    def should_be_challenging_dom_page(self):
        text = self.page.locator(ChallengingDomLocators.PAGE_NAME)
        self.expect(text, f'should be present Challenging DOM page, but present "{text.inner_text()}"').to_contain_text(
            'Challenging DOM')
        #assert 'Challenging DOM' in text, f'Should be Challenging DOM, but {text}'

    def should_check_buttons(self):
        for i in range(3):
            button = self.page.locator(ChallengingDomLocators.FIRST_BUTTON)
            button.click()
            button = self.page.locator(ChallengingDomLocators.SECOND_BUTTON)
            button.click()
            button = self.page.locator(ChallengingDomLocators.THIRD_BUTTON)
            button.click()