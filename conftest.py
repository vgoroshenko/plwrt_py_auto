import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Page




@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()
    # with sync_playwright() as p:
    #     if request.param == 'chromium':
    #         browser = p.chromium.launch()
    #     elif request.param == 'firefox':
    #         browser = p.firefox.launch()
    #     elif request.param == 'webkit':
    #         browser = p.webkit.launch()
    #
    #     context = browser.new_context()
    #     page = context.new_page()
    #
    #     yield {'browser': browser, 'context': context, 'page': page}
    #     page.close()
    #     browser.close()