import pytest
from pytest_bdd import given, when, then
from Config.settings import Environment
from Drivers.browser import driver
from Pages.Dashboard import Dashboard
import time
from Utils.custom_waits import wait_and_click, wait_till_element_appears
from Pages.LoginPage import Login


@pytest.fixture(scope="session", autouse=True)
def posttest():
    yield driver
    driver.quit()


@given("User opens the Automation Practice website")
def logging_in():
    driver.get(Environment.url)
    wait_till_element_appears("xpath", Dashboard.lbl_dresses)


@when("User clicks Sign-in Page")
def username_password():
    wait_and_click("xpath", Dashboard.btn_sign_in)


@then("User logs out")
def account_sign_out():
    wait_and_click("class", Login.btn_logout)
