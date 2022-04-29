import time
import pytest
from Config.settings import Environment
from Drivers.browser import driver
from faker import Faker
from pytest_bdd import scenario, given, when, then, parsers
from Pages.LoginPage import Login
from Pages.Dashboard import Dashboard
from Pages.Account import Account

from Utils.custom_waits import wait_and_click, \
    wait_till_element_appears, \
    load_send_keys

fake = Faker()
Faker.seed(0)


@pytest.mark.run(order=1)
@pytest.mark.login
@scenario('../../../Features/test_0001_Login.feature',
          'User is trying to Login using the username and password textbox')
def test_login_page():
    pass


@given("User opens the Automation Practice website")
def logging_in():
    driver.get(Environment.url)
    wait_till_element_appears("xpath", Dashboard.dresses)


@when("User clicks Sign-in Page")
def username_password():
    wait_and_click("xpath", Dashboard.sign_in, 0.1)


@when("User enters username and password and clicks sign-in button")
def username_password():
    load_send_keys("id", Login.txt_email, Environment.email)
    load_send_keys("id", Login.txt_email, Environment.password)
    wait_and_click("id", Login.btn_signin)


@then("Verify the name is appearing in home page")
def name_check():
    name = driver.find_element_by_xpath(Account.acc_name).text
    name_2 = Environment.f_name+" "+Environment.l_name
    assert name == name_2

@then("User is logged-in")
def logged_in():
    assert_homepage()


@pytest.mark.noautofixt
@pytest.mark.login_invalid_emailcases
@scenario('../../../Features/test_0001_Login.feature', 'Login functionality with Negative emailid  and valid password')
def test_login_invalidEmail_Cases():
    pass


@given('User opens login in page')
def launching_the_Url():
    driver.get(Environment.url)


@when('the User enters "<invalid_email>" into username and valid credential on the other textbox')
def login_with_negative_email(invalid_email):
    load_send_keys("id", Login_Page.txtbox_username, invalid_email)
    load_send_keys("id", Login_Page.txtbox_password, Environment.password)
    wait_and_click("id", Login_Page.btn_login)
    time.sleep(2)  # not a big fan of sleep,but here sleep wins over any wait method


@then(parsers.parse('verify {wrong_cred} will display a "<warning_message>" under the textbox'))
def validate_emailwarning_message(wrong_cred, warning_message):
    if wrong_cred == "wrong_email":
        wait_till_element_appears("xpath", Login_Page.errmsg_username, 0.9)
        actual_email_warning = driver.find_element_by_xpath(Login_Page.errmsg_username).text
        assert actual_email_warning == warning_message

    elif wrong_cred == "wrong_password":
        wait_till_element_appears("xpath", Login_Page.errmsg_password, 0.9)
        actual_password_warning = driver.find_element_by_xpath(Login_Page.errmsg_password).text
        assert actual_password_warning == warning_message


@pytest.mark.noautofixt
@pytest.mark.login_invalid_passwordcases
@scenario('../../../Features/test_0001_Login.feature', 'Login functionality with Negative password  and valid email')
def test_login_invalidPassword_Cases():
    pass


@when('the User enters "<invalid_password>" into password and valid credential on the other textbox')
def login_with_negative_email(invalid_password):
    load_send_keys("id", Login_Page.txtbox_username, Environment.username)
    load_send_keys("id", Login_Page.txtbox_password, invalid_password)
    wait_and_click("id", Login_Page.btn_login)
    time.sleep(2)  # not a big fan of sleep,but here sleep wins over any wait method