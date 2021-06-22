from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
import time


@given('The Guest is on the employee Page')
def employee_page(context):
    context.driver.get('file:///C:/Users/amin/Desktop/day01/01/project11%20front%20end/Employee.html')
    context.driver.implicitly_wait(3)
    time.sleep(1)


@when('The Guest types {amount} into the amount bar')
def step_impl(context, amount: str):
    context.employee.amount_bar().send_keys(amount)
    time.sleep(1)

@when('The Guest types {reason} into the reason bar')
def step_impl(context, reason: str):
    context.employee.reason_bar().send_keys(reason)
    time.sleep(1)

@when('The Guest types {status} into the status bar')
def step_impl(context, status: str):
    context.employee.status_bar().send_keys(status)
    time.sleep(1)

@when('The Guest clicks on the add button')
def step_impl(context):
    context.employee.add_request_button().click()
    time.sleep(1)

@Then('The prompt alert text should be {text}')
def step_impl(context, text: str):
    alert = context.driver.switch_to.alert
    assert text == alert.text
    time.sleep(1)

