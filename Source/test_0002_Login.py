import time
import pytest
import allure
from Config.settings import Environment
from Drivers.browser import driver
from pytest_bdd import scenario, given, when, then, parsers
from Pages.LoginPage import Login
from Pages.Account import Account

from Utils.custom_waits import wait_and_click, \
    load_send_keys, get_text


@pytest.mark.run(order=1)
@pytest.mark.login
@allure.feature('User is trying to Login using the username and password textbox')
@scenario('../Features/test_0002_Login.feature',
          'User is trying to Login using the username and password textbox')
def test_login_page():
    pass


@when("User enters username and password and clicks sign-in button")
def username_password():
    load_send_keys("id", Login.txt_email, Environment.email)
    load_send_keys("id", Login.txt_password, Environment.password)
    wait_and_click("id", Login.btn_signin)


@then("Verify the name is appearing in home page")
def name_check():
    actual_name = driver.find_element_by_xpath(Account.lbl_acc_name).text
    expected_name = Environment.f_name+" "+Environment.l_name
    assert actual_name == expected_name


@pytest.mark.run(order=2)
@pytest.mark.login
@allure.feature('Login functionality with wrong emailid and valid password')
@scenario('../Features/test_0002_Login.feature',
          'Login functionality with wrong emailid and valid password')
def test_login_wrong_username():
    pass


@when(parsers.parse('User enters "{invalid_email}" into username and valid password on the other textbox'))
def login_with_negative_email(invalid_email):
    load_send_keys("id", Login.txt_email, invalid_email)
    load_send_keys("id", Login.txt_password, Environment.password)
    wait_and_click("id", Login.btn_signin)
    time.sleep(2)


@then (parsers.parse('Verify the "{warning_message}"'))
def validate_warning_message(warning_message):
    assert warning_message == get_text("xpath", Login.lbl_error)


@pytest.mark.run(order=3)
@pytest.mark.login
@allure.feature('Login functionality with wrong password and valid emai')
@scenario('../Features/test_0002_Login.feature',
          'Login functionality with wrong password and valid emai')
def test_login_wrong_password():
    pass


@when(parsers.parse('User enters valid username into username and "{invalid_password}" into the other textbox'))
def login_with_negative_email(invalid_password):
    load_send_keys("id", Login.txt_email, Environment.email)
    load_send_keys("id", Login.txt_password, invalid_password)
    wait_and_click("id", Login.btn_signin)
    time.sleep(2)
