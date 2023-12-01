from pages.locators import UrlLocators
from playwright.sync_api import expect, Page


class BasePage:
    def __init__(self, page=Page, url=UrlLocators.MAIN_URL, timeout=4):
        self.page = page
        self.url = url
        self.open()
        self.expect = expect

    def open(self):
        self.page.goto(self.url)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    def select_element_with_value(self, locator, value):
        self.page.locator(locator).select_option(value=value)


    def get_alert_text(self):
        test = []
        #self.page.on("dialog", lambda dialog: print(dialog.message))
        #print(test)
        return test
