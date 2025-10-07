import time

from selenium.webdriver.common.by import By

from Pages.basic_action import BasicActions


class AdminPage(BasicActions):
    edit_user_role = (By.XPATH,'(//div[@class="oxd-table-row oxd-table-row--with-border"])[2]/div[3]/div')
    edit_status = (By.XPATH,'(//div[@class="oxd-table-row oxd-table-row--with-border"])[2]/div[5]/div')
    edit_employee_name = (By.XPATH,'(//div[@class="oxd-table-row oxd-table-row--with-border"])[2]/div[4]/div')
    edit_username = (By.XPATH,'(//div[@class="oxd-table-row oxd-table-row--with-border"])[2]/div[2]/div')
    username_textbox = (By.XPATH,'(//input[@class="oxd-input oxd-input--active"])[2]')
    userrole_arrow = (By.XPATH,'(//div[@class="oxd-select-text--after"])[1]')
    userrole_value = (By.XPATH,"//span[text()='{}']")
    emp_text_field = (By.XPATH,"//input[@placeholder='Type for hints...']")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def first_row_data(self):
        # self.wait_for_object(self.first_edit_button)
        # self.click_me(self.first_edit_button)
        self.wait_for_object(self.edit_user_role)
        userRole = self.get_text(self.edit_user_role)
        userStatus = self.get_text(self.edit_status)
        emp_name =self.get_text(self.edit_employee_name)
        username = self.get_text(self.edit_username)
        return username , userRole  , emp_name , userStatus

    def search_functionality(self, username, userrole):
        self.wait_for_object(self.username_textbox)
        self.type_words(self.username_textbox, username)
        self.click_me(self.userrole_arrow)
        time.sleep(2)
        print(self.userrole_value[1].format(userrole))
        act_userrole = (self.userrole_value[0] , self.userrole_value[1].format(userrole))
        print(act_userrole)
        self.wait_for_object(act_userrole)
        self.click_by_javascript(act_userrole)
        time.sleep(5)




