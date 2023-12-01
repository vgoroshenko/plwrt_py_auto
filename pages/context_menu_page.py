from .base.base_page import BasePage
from .locators import ContextMenuLocators


class ContextMenu(BasePage):
    def go_to_page(self):
        link = self.page.locator(ContextMenuLocators.CONTEXT_PAGE)
        link.click()

    def press_box_button(self):
        button = self.page.locator(ContextMenuLocators.BOX_BUTTON)
        button.click(button='right')

    def should_be_correct_page(self):
        text = self.page.locator(ContextMenuLocators.PAGE_NAME)
        self.expect(text, f'should be present Context Menu page, but present "{text.inner_text()}"').to_contain_text(
            'Context Menu')
        # assert 'Context Menu' in text, f'should be "Context Menu", but "{text}"'

    def should_be_correct_context(self):
        alert_text = self.page.evaluate('() => {return window.alert; }')
        assert 'context menu' in alert_text, f'should be context menu, but {alert_text}'

    # def should_alert_present(self):
    #     assert self.alert_is_present(), 'should alert present, but not'
