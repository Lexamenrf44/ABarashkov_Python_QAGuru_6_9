import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)

# Basic setup
def browser_setup():
    browser.config.window_height = '1680'
    browser.config.window_width = '1050'
