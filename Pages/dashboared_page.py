import time

from selenium.webdriver.common.by import By

from Pages.basic_action import BasicActions


class DashboardPage(BasicActions):
    dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_dashboard_is_present(self):
        assert self.element_displayed(self.dashboard_text)