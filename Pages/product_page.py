import time

from selenium.webdriver.common.by import By

from Pages.basic_action import BasicActions


class ProductPage(BasicActions):
    product_text_field = (By.XPATH, '(//div[@data-test="inventory-item-name"])[1]')
    price_text_field = (By.XPATH, "(//div[@data-test='inventory-item-price'])[1]")
    add_to_cart_btn = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    remove_btn = (By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    shopping_cart_link = (By.XPATH, '//a[@data-test="shopping-cart-link"]')
    all_product = (By.XPATH, '//div[@class="inventory_item_description"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def product_name(self):
        value  = self.get_text(self.product_text_field)
        return value

    def product_price(self):
        value  = self.get_text(self.price_text_field)
        return value


    def click_on_add_to_cart(self):
        self.wait_for_object(self.add_to_cart_btn)
        self.click_me(self.add_to_cart_btn)

    def verify_remove_btn(self):
        self.wait_for_object(self.remove_btn)
        assert self.element_displayed(self.remove_btn)

    def click_on_shipping_link(self):
        self.wait_for_object(self.shopping_cart_link)
        self.click_me(self.shopping_cart_link)

    def count_product(self):
        products = self.get_web_elements(self.all_product)
        return len(products)

