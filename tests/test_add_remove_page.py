from pages.add_remove_page import AddRemove

def test_go_add_remove_page(page):
    page = AddRemove(page)
    page.go_to_module()
    page.should_be_add_remove_page_present()

def test_add_element(page):
    page = AddRemove(page)
    page.go_to_module()
    page.press_add_button()
    page.should_be_remove_button_present()

def test_remove_element(page):
    page = AddRemove(page)
    page.go_to_module()
    page.press_add_button()
    page.press_delete_button()
    page.should_removed_element()

def test_add_multiple_elements(page):
    page = AddRemove(page)
    page.go_to_module()
    page.press_add_button_count(2)
    page.should_be_present_remove_buttons_count(2)

def test_remove_multiple_elements(page):
    page = AddRemove(page)
    page.go_to_module()
    page.press_add_button_count(2)
    page.press_delete_button()
    page.press_delete_button()
    page.should_be_present_remove_buttons_count(0)

