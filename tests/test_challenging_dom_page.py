from pages.challening_dom_page import ChallengingDom

def test_present_challenging_dom_page(page):
    page = ChallengingDom(page)
    page.go_to_page()
    page.should_be_challenging_dom_page()

def test_unique_elements_after_click_button(page):
    page = ChallengingDom(page)
    page.go_to_page()
    page.should_check_buttons()