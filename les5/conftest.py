import pytest
from selene.support.shared import browser


@pytest.fixture
def browser_setup():
    browser.config.window_width = 1440
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'