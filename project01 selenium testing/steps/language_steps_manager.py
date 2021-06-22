from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
import time

@when('The Guest types {id} into the id bar')
def step_impl(context, id: int):
    context.manager.id_bar().send_keys(id)


@when('The Guest types {status} into the request status bar')
def step_impl(context, status: str):
    context.manager.status_bar().send_keys(status)


@when('The Guest clicks on the update button')
def step_impl(context):
    time.sleep(2)
    context.manager.update_button().click()
    time.sleep(2)
