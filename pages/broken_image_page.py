from pages.locators import BrokenImagesLocators
from pages.base.base_page import BasePage


class ImageNotFoundError(Exception):
    pass


class BrokenImages(BasePage):

    def go_to_module(self):
        link = self.page.locator(BrokenImagesLocators.BROKEN_IMAGE_PAGE)
        link.click()

    def should_present_broken_image_page(self):
        text = self.page.locator(BrokenImagesLocators.PAGE_NAME)
        self.expect(text, f'should be present Broken Images page, but present "{text.inner_text()}"').to_contain_text('Broken Images')
        #assert 'Broken Images' in text, f'should be present Broken Images page, but present "{text}"'

    def should_not_present_errors(self):
        self.page.expect_console_message()
        logs = []
        def handle_console_message(msg):
            print(f"Сообщение из консоли: {msg.text()}")
            logs.append(msg.text())
        self.page.on('console', handle_console_message)
        errors = [log for log in logs if
                  log['level'] == 'SEVERE' and 'favicon.ico' not in log['message'] and 'chrome-error' not in log[
                      'message']]
        print(errors)
        if errors:
            raise ImageNotFoundError(f'Есть ошибки')
