import time

from selenium.webdriver.common.by import By

from Pages.basic_action import BasicActions


class CheckoutPage(BasicActions):
    firstName_text_box = (By.ID, "first-name")
    lastName_text_box = (By.ID, "last-name")
    postalCode_text_box = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    tax_price_text = (By.CSS_SELECTOR, "[data-test='tax-label']")
    total_price_text = (By.CSS_SELECTOR, "[data-test='total-label']")
    finish_btn = (By.ID, "finish")
    succeessful_text = (By.CSS_SELECTOR, "[data-test='complete-header']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def enter_value_in_firstname(self, firstname, lastname, zipcode):
        self.wait_for_object(self.firstName_text_box)
        self.type_words(self.firstName_text_box, firstname)
        self.type_words(self.lastName_text_box, lastname)
        self.type_words(self.postalCode_text_box, zipcode)

    def click_on_continue_btn(self):
        self.wait_for_object(self.continue_btn)
        self.click_me(self.continue_btn)

    def fetch_tax_and_total_price(self):
        self.wait_for_object(self.tax_price_text)
        tax_price = self.get_text(self.tax_price_text)
        total_price = self.get_text(self.total_price_text)
        return tax_price   , total_price

    def click_on_finish_btn(self):
        self.wait_for_object(self.finish_btn)
        self.click_me(self.finish_btn)

    def fetch_successful_message(self):
        self.wait_for_object(self.succeessful_text)
        value = self.get_text(self.succeessful_text)
        return value