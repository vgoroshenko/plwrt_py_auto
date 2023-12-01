import pytest

from pages.context_menu_page import ContextMenu


def test_go_to_page(page):
    page = ContextMenu(page)
    page.go_to_page()
    page.should_be_correct_page()

@pytest.mark.xfail
def test_should_view_context(page):
    page = ContextMenu(page)
    page.go_to_page()
    page.press_box_button()
    page.should_be_correct_context()
    # page.alert_is_present()
    # page.alert_accept()
    # page.alert_is_not_present()
