from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Manager:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def id_bar(self):
        element: WebElement = self.driver.find_element_by_id("rrIdInput")
        return element

    def status_bar(self):
        element: WebElement = self.driver.find_element_by_id("statusInput")
        return element

    def update_button(self):
        element: WebElement = self.driver.find_element_by_id("updateBtn")
        return element
