import pytest

from Pages.dashboared_page import DashboardPage
from Pages.login_page import LoginPage
from util.common_util import *


class TestLoginPage:
    header = ["username", "password"]
    data = read_excel_data("logindata")

    @pytest.mark.usefixtures("open_browser_test_startup")
    @pytest.mark.parametrize(header, data)
    def test_with_multiple_data_login_feature(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.enter_user_name(username)
        login_page.enter_password(password)
        login_page.click_on_login()
        Dashboard_page = DashboardPage(self.driver)
        Dashboard_page.check_dashboard_is_present()


    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_login_feature(self):
        login_page = LoginPage(self.driver)
        login_page.enter_user_name(get_data_from_inputs("username"))
        login_page.enter_password(get_data_from_inputs("password"))
        login_page.click_on_login()
