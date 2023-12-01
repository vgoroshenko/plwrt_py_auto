import pytest

from pages.broken_image_page import BrokenImages

@pytest.mark.xfail #отсутствие_изображения
def test_go_to_broken_image():
    page = BrokenImages()
    page.go_to_module()
    page.should_present_broken_image_page()
    page.should_not_present_errors()