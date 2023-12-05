import pytest

from pages.file_uploader_page import FileUploader

def test_go_to_page(page):
    page = FileUploader(page)
    page.go_to_page()
    page.should_be_correct_page()

def test_upload_file(page):
    page = FileUploader(page)
    page.go_to_page()
    page.upload_file()
    page.should_be_uploaded_file()

@pytest.mark.xfail
def test_upload_drag_and_drop_file(page):
    page = FileUploader(page)
    page.go_to_page()
    page.drag_and_drop_file()
    page.click_upload()
    page.should_be_uploaded_file_drag()