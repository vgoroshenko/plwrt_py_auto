from pages.dropdown_page import Dropdown

def test_go_to_page(page):
    page = Dropdown(page)
    page.go_to_page()
    page.should_be_correct_page()

def test_select_dropdown_element(page):
    page = Dropdown(page)
    page.go_to_page()
    page.select_element_value(2)
    page.should_be_selected_second()

