from pages.form_authentication_page import FormAuthentication


def test_go_to_page(page):
    page = FormAuthentication(page)
    page.go_to_page()
    page.should_be_correct_page()


def test_login(page):
    page = FormAuthentication(page)
    page.go_to_page()
    page.set_username()
    page.set_password()
    page.click_login()
    page.should_be_correct_secure_area_page()
    page.should_be_success_login_message()


def test_logout(page):
    page = FormAuthentication(page)
    page.go_to_page()
    page.login()
    page.click_logout()
    page.should_be_correct_page()
    page.should_be_success_logout_message()


def test_failed_login(page):
    page = FormAuthentication(page)
    page.go_to_page()
    page.set_username()
    page.set_incorrect_password()
    page.click_login()
    page.should_be_failed_message()
    page.should_be_correct_page()
