from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Signin:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username_bar(self):
        element: WebElement = self.driver.find_element_by_id("floatingUsername")
        return element

    def password_bar(self):
        element: WebElement = self.driver.find_element_by_id("floatingPassword")
        return element

    def signin_button(self):
        element: WebElement = self.driver.find_element_by_id("helloBtn")
        return element
