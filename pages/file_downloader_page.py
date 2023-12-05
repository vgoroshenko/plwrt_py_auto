import os
import getpass
from pages.locators import FileDownloadLocators, BasePageLocators
from pages.base.base_page import BasePage


class FileDownloader(BasePage):

    download_path = []

    def go_to_page(self):
        link = self.page.locator(FileDownloadLocators.LOADED_PAGE)
        link.click()

    def download_file(self):
        with self.page.expect_download() as download_info:
            button = self.page.locator(FileDownloadLocators.FILE)
            button.click()
        self.download_path = download_info.value

    def should_be_downloaded_file(self):
        file_path = os.path.join(self.download_path.path())
        assert os.path.isfile(file_path), f'should be downloaded file, but not'

    def should_be_correct_page(self):
        text = self.get_text(BasePageLocators.PAGE_NAME)
        correct_text = 'File Downloader'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'
