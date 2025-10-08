import time

from selenium.webdriver.common.by import By

from Pages.basic_action import BasicActions


class CartPage(BasicActions):
    product_text_field = (By.XPATH, '(//div[@data-test="inventory-item-name"])[1]')
    price_text_field = (By.XPATH, "(//div[@data-test='inventory-item-price'])[1]")
    checkout_btn = (By.ID, "checkout")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def product_name(self):
        value  = self.get_text(self.product_text_field)
        return value

    def product_price(self):
        value  = self.get_text(self.price_text_field)
        return value

    def click_on_checkout_btn(self):
        self.wait_for_object(self.checkout_btn)
        self.click_me(self.checkout_btn)

