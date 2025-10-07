from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasicActions:

    def __init__(self, driver = None):
        self.driver = driver

    def open_my_browser(self, browser=None):  # firefox
        try:
            if browser == "chrome":
                self.driver = self.open_chrome()
            elif browser == "firefox":
                self.driver = self.open_firefox()
            elif browser == "edge":
                self.driver = self.open_edge()
            else:
                self.driver = self.open_chrome()
        except Exception:
            print("browser not opened")
        return self.driver

    def open_chrome(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def open_firefox(self):
        self.driver = webdriver.Firefox()
        return self.driver

    def open_edge(self):
        self.driver = webdriver.Edge()
        return self.driver

    def go_to_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(f"exception in url {e}")

    def maximize_browser_window(self):
        try:
            self.driver.maximize_window()
        except Exception as e:
            print(f"exception occures while maximize the window {e}")


    def close_browser(self):
        self.driver.close()

    def type_words(self, locator, text):
        element = self.get_web_element(locator)
        element.clear()
        element.send_keys(text)

    def get_web_element(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        return element

    def get_web_elements(self, locator):
        elements = self.driver.find_elements(locator[0], locator[1])
        return elements

    def click_me(self, locator):
        element = self.get_web_element(locator)
        element.click()

    def wait_for_object(self, locator, timeout= 10):
        wait = WebDriverWait(self.driver ,timeout)
        wait.until(EC.presence_of_element_located(locator))

    def element_displayed(self, locator, timeout=10):
        self.wait_for_object(locator, timeout)
        flag = self.get_web_element(locator).is_displayed()
        return flag

    def drag_drop(self, locator1, locator2 ):
        action = ActionChains(self.driver)
        source = self.get_web_element(locator1)
        target = self.get_web_element(locator2)
        action.drag_and_drop(source, target).perform()

    def select_value(self, locator, text):
        element = self.get_web_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def get_text(self, locator):
        try:
            element = self.get_web_element(locator)
            value = element.text
        except Exception as e:
            print(f" in get text got expection {e}")
        return value

    def click_by_javascript(self, locator):
        element = self.get_web_element(locator)
        self.driver.execute_script("arguments[0].click();", element)


