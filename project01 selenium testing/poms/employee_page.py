from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Employee:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def amount_bar(self):
        element: WebElement = self.driver.find_element_by_id("amountInput")
        return element

    def status_bar(self):
        element: WebElement = self.driver.find_element_by_id("statusInput")
        return element

    def reason_bar(self):
        element: WebElement = self.driver.find_element_by_id("reasonInput")
        return element

    def add_request_button(self):
        element: WebElement = self.driver.find_element_by_id("btn")
        return element