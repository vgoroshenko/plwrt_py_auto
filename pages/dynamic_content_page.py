import time

from .base.base_page import BasePage
from .locators import DynamicContentLocators, BasePageLocators


class DynamicContent(BasePage):

    def change_content(self):
        button = self.page.locator(DynamicContentLocators.CHANGE_CONTENT_BUTTON)
        button.click()
        time.sleep(2)

    def go_to_page(self):
        link = self.page.locator(DynamicContentLocators.DYNAMIC_CONTENT_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(BasePageLocators.PAGE_NAME)
        correct_text = 'Dynamic Content'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_changed_content_after_change(self):
        text_elements = self.page.locator(DynamicContentLocators.ALL_TEXT_CONTENT_ELEMENTS).all()
        self.change_content()
        elements2 = [i.inner_text() for i in self.page.locator(DynamicContentLocators.ALL_TEXT_CONTENT_ELEMENTS).all()]
        flag = True
        for i in elements2:
            if i in text_elements:
                flag = False
        assert flag, 'should be changed text, but not'

    def should_be_not_changed_second_row_content(self):
        time.sleep(1)
        elements = self.page.locator(DynamicContentLocators.ALL_TEXT_CONTENT_ELEMENTS).all()
        text = elements[0].inner_text()
        self.change_content()
        elements = self.page.locator(DynamicContentLocators.ALL_TEXT_CONTENT_ELEMENTS).all()
        text_after = elements[0].inner_text()
        assert text == text_after, f'should be not changed text, but yes {text[0:10]} and {text_after[0:10]}'


