import pytest

from Pages.basic_action import BasicActions
from util.common_util import get_data_from_inputs

global driver
driver = None


@pytest.fixture(scope="function")
def open_browser_test_startup(request):
    browser = get_data_from_inputs("browser")  #chrome
    global driver
    basic_action = BasicActions()
    driver = basic_action.open_my_browser(browser)
    url = get_data_from_inputs("url")
    basic_action.go_to_url(url)
    basic_action.maximize_browser_window()
    request.cls.driver = driver
    yield
    basic_action.close_browser()
