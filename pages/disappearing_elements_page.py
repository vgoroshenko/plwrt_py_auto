from .base.base_page import BasePage
from .locators import DisappearingElementsLocators, BasePageLocators


class DisappearingElements(BasePage):

    def go_to_page(self):
        link = self.page.locator(DisappearingElementsLocators.DISAPPERATING_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(BasePageLocators.PAGE_NAME)
        correct_text = 'Disappearing Elements'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_changed_buttons_count(self):
        start_len_button_list = self.page.locator(DisappearingElementsLocators.BUTTON_LIST).count()
        after_reload_len = start_len_button_list
        flag = 0
        while start_len_button_list == after_reload_len:
            self.page.reload()
            after_reload_len = self.page.locator(DisappearingElementsLocators.BUTTON_LIST).count()
            print(after_reload_len)
            flag += 1
            if flag == 10:
                assert False, 'buttons count not changed'
