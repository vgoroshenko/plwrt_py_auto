from pages.ab_testing_page import ABPage


def test_ab_page(page):
    page = ABPage(page)
    page.go_to_ab_page()
    page.should_be_ab_page()
