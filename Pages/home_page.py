import time

from selenium.webdriver.common.by import By

from Pages.basic_action import BasicActions


class HomePage(BasicActions):
    admin_sub_menu = (By.XPATH, "//span[text()='Admin' or '管理员']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_admin_menu(self):
        self.wait_for_object(self.admin_sub_menu)
        self.click_me(self.admin_sub_menu)