import pytest

from pages.file_downloader_page import FileDownloader

def test_go_to_page(page):
    page = FileDownloader(page)
    page.go_to_page()
    page.should_be_correct_page()

#@pytest.mark.xfail
def test_file_download(page):
    page = FileDownloader(page)
    page.go_to_page()
    page.download_file()
    page.should_be_downloaded_file()
