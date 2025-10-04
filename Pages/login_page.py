import time

from selenium.webdriver.common.by import By

from Pages.basic_action import BasicActions


class LoginPage(BasicActions):
    username_text_field = (By.XPATH, "//input[@name ='username']")
    password_text_field = (By.XPATH, "//input[@name ='password']")
    login_btn = (By.XPATH, "//button[normalize-space() ='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_user_name(self, username):
        self.wait_for_object(self.username_text_field)
        self.type_words(self.username_text_field,username)

    def enter_password(self, password):
        self.wait_for_object(self.password_text_field)
        self.type_words(self.password_text_field,password)

    def click_on_login(self):
        self.click_me(self.login_btn)

