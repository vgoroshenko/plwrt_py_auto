import pytest
import allure
import os
import time
from playwright.sync_api import Playwright, sync_playwright, expect, Page


@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, args=["--no-sandbox", "--disable-gpu"],
                                             ignore_default_args=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
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


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed or 'call' and rep.passed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'page' in item.fixturenames:
                    page = item.funcargs['page']
                    allure.attach(
                        page.screenshot(),
                        name='step_screenshot_' + f'{time.asctime().split()[-2]}',
                        attachment_type=allure.attachment_type.TEXT and allure.attachment_type.PNG
                    )
                else:
                    print('Fail to take screen-shot')
                    return
                # allure.attach(
                #     page.screenshot(),
                #     name='console log:',
                #     attachment_type=allure.attachment_type.TEXT and allure.attachment_type.PNG
                # )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture(autouse=True)
def screenshot_on_step(request, page):
    def take_screenshot():
        screenshot_path = f"./reports/{request.function.__name__}_{request.node.name}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path,
                           name="Screenshot" + f' {time.asctime().split()[-2]}',
                           attachment_type=allure.attachment_type.TEXT and allure.attachment_type.PNG)

    request.addfinalizer(take_screenshot)
