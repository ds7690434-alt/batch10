import time

import pytest

from Pages.admin_page import AdminPage
from Pages.cart_page import CartPage
from Pages.dashboared_page import DashboardPage
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from util.common_util import *


class TestProductPage:
    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_verify_product_functionality(self):
        login_page = LoginPage(self.driver)
        login_page.enter_user_name(get_data_from_inputs("username"))
        login_page.enter_password(get_data_from_inputs("password"))
        login_page.click_on_login()
        productPage = ProductPage(self.driver)
        product_name =productPage.product_name()
        product_price =  productPage.product_price()
        productPage.click_on_add_to_cart()
        productPage.verify_remove_btn()
        productPage.click_on_shipping_link()
        cartPage = CartPage(self.driver)
        cart_page_product_name = cartPage.product_name()
        cart_page_product_price = cartPage.product_price()
        time.sleep(5)
        assert  product_name == cart_page_product_name
        assert  product_price == cart_page_product_price

    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_verify_product_count(self):
        login_page = LoginPage(self.driver)
        login_page.enter_user_name(get_data_from_inputs("username"))
        login_page.enter_password(get_data_from_inputs("password"))
        login_page.click_on_login()
        productPage = ProductPage(self.driver)
        product_count  = productPage.count_product()
        assert  product_count == get_data_from_inputs("product_count")