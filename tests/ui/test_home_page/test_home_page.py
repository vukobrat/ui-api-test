import pytest

from config.config import APP_URL
from src.pages.HomePage import HomePage


@pytest.mark.ui
def test_home_page(browser):
    home_page = HomePage(browser)

    assert home_page.button_homepage_logo.is_displayed()
    assert browser.title == "Software design and development for the world's biggest brands | Symphony"
    assert browser.current_url == APP_URL
