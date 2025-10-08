import pytest

from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.common_action import fetch_number_from_string
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from util.common_util import *

class TestEndTOEnd:
    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_validatet_end_to_end_functionality(self):
        login_page = LoginPage(self.driver)
        login_page.enter_user_name(get_data_from_inputs("username"))
        login_page.enter_password(get_data_from_inputs("password"))
        login_page.click_on_login()
        productPage = ProductPage(self.driver)
        actual_price = productPage.product_price()
        productPage.click_on_add_to_cart()
        productPage.click_on_shipping_link()
        cartPage = CartPage(self.driver)
        cartPage.click_on_checkout_btn()
        checkout = CheckoutPage(self.driver)

        value = read_excel_data("testdata")
        checkout.enter_value_in_firstname(value[0][0], value[0][1], value[0][2])
        checkout.click_on_continue_btn()
        tax_price , total_price = checkout.fetch_tax_and_total_price()

        tax_price = fetch_number_from_string(tax_price)
        total_price = fetch_number_from_string(total_price)
        actual_price = fetch_number_from_string(actual_price)
        assert actual_price + tax_price  == total_price
        checkout.click_on_finish_btn()
        success_mesage  = checkout.fetch_successful_message()
        assert success_mesage == "Thank you for your order!"