from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
import time


@given('The Guest is on the logging Home Page')
def open_up_signin_page(context):
    context.driver.get('file:///C:/Users/amin/Desktop/day01/01/project11%20front%20end/Sign_in.html')
    context.driver.implicitly_wait(3)
    time.sleep(1)


@when('The Guest types abc into the username bar')
def step_impl(context):
    context.signin.username_bar().send_keys('abc')


@when('The Guest types 123 into the password bar')
def step_impl(context):
    context.signin.password_bar().send_keys(123)


@when('The Guest clicks on the signin button')
def step_impl(context):
    time.sleep(1)
    context.signin.signin_button().click()
    time.sleep(1)


@when('The guest clicks ok on  alert prompt')
def step_impl(context):
    alert = context.driver.switch_to.alert
    alert.accept()
    time.sleep(1)


@Then('The guest should be on employee page')
def step_impl(context):
    title = context.driver.title
    assert title == "Employees"


@Then('The alert prompts and say welcome to employee')
def step_impl(context):
    alert = context.driver.switch_to.alert
    text = alert.text
    assert text == 'Dear Employee Albus4 wlcome'
    time.sleep(1)


@when('The Guest types xyz into the password bar')
def step_impl(context):
    context.signin.password_bar().send_keys('xyz')


@Then('The alert prompts and say welcome to manager')
def step_impl(context):
    alert = context.driver.switch_to.alert
    text = alert.text
    assert text == 'Dear Manager Amin1 wlcome'


@Then('The guest should be on manager page')
def step_impl(context):
    title = context.driver.title
    assert title == "Manager"
    time.sleep(1)


@when('The Guest types abcd into the username bar')
def step_impl(context):
    context.signin.username_bar().send_keys('abcd')


@Then('The alert prompts and say username or password is not correct')
def step_impl(context):
    alert = context.driver.switch_to.alert
    text = alert.text
    assert text == ' Your username or password does not match.'
    time.sleep(1)
