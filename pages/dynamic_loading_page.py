from .locators import DynamicallyLoadedLocators, BasePageLocators
from .base.base_page import BasePage


class DynamicallyLoaded(BasePage):

    def click_example_1(self):
        button = self.page.locator(DynamicallyLoadedLocators.EXAMPLE_ONE_BUTTON)
        button.click()

    def click_example_2(self):
        button = self.page.locator(DynamicallyLoadedLocators.EXAMPLE_TWO_BUTTON)
        button.click()

    def click_start(self):
        button = self.page.locator(DynamicallyLoadedLocators.START_BUTTON)
        button.click()

    def go_to_page(self):
        link = self.page.locator(DynamicallyLoadedLocators.DYNAMICALLY_LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(BasePageLocators.PAGE_NAME)
        correct_text = 'Dynamically Loaded'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_load_bar_present(self):
        load_bar = self.page.locator(DynamicallyLoadedLocators.LOADING_BAR)
        assert load_bar.is_visible(), 'should be load bar present, but not'

    def should_be_load_bar_disappeared(self):
        assert self.is_disappeared(DynamicallyLoadedLocators.LOADING_BAR, 8000), 'should be load bar dont present, but yes'

    def should_be_hello_word_present(self):
        final_text = self.get_text(DynamicallyLoadedLocators.FINISH_TEXT)
        text = 'Hello World!'
        assert text in final_text, f'should be {text}, but present {final_text}'
