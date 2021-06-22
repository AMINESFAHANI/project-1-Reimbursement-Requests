from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from poms.employee_page import Employee
from poms.logging_page import Signin
from poms.manager_page import Manager




def before_all(context: Context):

    context.driver: WebDriver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')


    context.signin = Signin(context.driver)
    context.employee = Employee(context.driver)
    context.manager = Manager(context.driver)
    print("I run before ANY scenarios")


def after_all(context):
    print("I run after all scenarios")
    context.driver.quit()
