import time

import pytest

from Pages.admin_page import AdminPage
from Pages.dashboared_page import DashboardPage
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from util.common_util import *


class TestLoginPage:
    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_verify_username_functionality(self):
        login_page = LoginPage(self.driver)
        login_page.enter_user_name(get_data_from_inputs("username"))
        login_page.enter_password(get_data_from_inputs("password"))
        login_page.click_on_login()
        homepage = HomePage(self.driver)
        homepage.click_on_admin_menu()
        adminPage = AdminPage(self.driver)
        username, userRole, emp_name, userStatus = adminPage.first_row_data()
        adminPage.search_functionality(username, userRole)
