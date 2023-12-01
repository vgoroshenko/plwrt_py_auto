import pytest

from pages.basic_auth_page import BasicAuth

@pytest.mark.xfail
def test_unsuccessful_basic_auth_page(page):
    page = BasicAuth(page)
    page.go_to_failed_module()
    page.should_be_present_failed_message()
    
def test_success_basic_auth_page(page):
    page = BasicAuth(page)
    page.go_to_module()
    page.should_be_success_basic_auth_page()

