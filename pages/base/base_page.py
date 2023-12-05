from pages.locators import UrlLocators
from playwright.sync_api import expect, Page, TimeoutError


class BasePage:
    def __init__(self, page, url=UrlLocators.MAIN_URL):
        timeout = 20000
        page.set_default_navigation_timeout(timeout)
        page.set_default_timeout(timeout)
        self.page = page
        self.url = url
        self.expect = expect
        self.open()

    def open(self):
        self.page.goto(self.url)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    def select_element_with_value(self, locator, value):
        self.page.locator(locator).select_option(value=value)

    def is_disappeared(self, element_selector, timeout=4000):
        try:
            self.page.wait_for_selector(element_selector, state='hidden', timeout=timeout)
        except TimeoutError:
            return False
        return self.page.is_hidden(element_selector)

    def is_element_present_timeout(self, element_selector, timeout=4000):
        try:
            self.page.wait_for_selector(element_selector, timeout=timeout)
        except TimeoutError:
            return False
        return self.page.locator(element_selector).is_visible()


    def get_alert_text(self):
        test = []
        #self.page.on("dialog", lambda dialog: print(dialog.message))
        #print(test)
        return test
