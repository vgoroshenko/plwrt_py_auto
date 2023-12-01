from pages.disappearing_elements_page import DisappearingElements


def test_go_to_page(page):
    page = DisappearingElements(page)
    page.go_to_page()
    page.should_be_correct_page()

def test_change_element_counts(page):
    page = DisappearingElements(page)
    page.go_to_page()
    page.should_be_changed_buttons_count()