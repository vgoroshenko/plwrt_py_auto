import pytest
import allure
import os
import time
from playwright.sync_api import Playwright, sync_playwright, expect, Page

# @pytest.fixture(scope="session", params=['chromium', 'firefox', 'webkit'])
# def page(request):
#     with sync_playwright() as p:
#         browser_type = getattr(p, request.param)
#         browser = browser_type.launch(headless=True, args=["--no-sandbox", "--disable-gpu"])
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         context.close()
#         page.close()


# @pytest.fixture(scope="session")
# def browsers():
#     with sync_playwright() as p:
#
#         browsers = {
#             "chromium": p.chromium.launch(headless=True),
#             "firefox": p.firefox.launch(headless=True, args=["--no-sandbox", "--disable-gpu"]),
#             "webkit": p.webkit.launch(headless=True, args=["--no-sandbox", "--disable-gpu"])
#         }
#         yield browsers
#         for browser in browsers.values():
#             browser.close()
#
# #@pytest.fixture(params=["chromium", "firefox", "webkit"])
# @pytest.fixture(params=["chromium"])
# def page(request, browsers):
#     browser_type = request.param
#     if browser_type not in browsers:
#         raise ValueError(f"Invalid browser type: {browser_type}")
#     browser = browsers[browser_type]
#     context = browser.new_context()
#     page = browser.new_page()
#     yield page
#     context.close()
#     page.close()



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
