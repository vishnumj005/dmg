import pytest
import random
import allure

from Config.settings import Environment
from Drivers.browser import driver
from pytest_bdd import scenario, when, then
from Pages.Account import Account
from Pages.Registration import Form
from Utils.custom_waits import wait_and_click, \
    wait_till_element_appears, \
    load_send_keys, select_option_by_index


@pytest.mark.run(order=1)
@pytest.mark.registartion
@allure.feature('To test the Registration process')
@scenario('../Features/test_0001_Registration.feature', 'To test the Registration process')
def test_registration_page():
    pass


@when("User clicks create account")
def create_account():
    load_send_keys("xpath", Account.txt_new_email, Environment.signup_email)
    wait_and_click("xpath", Account.btn_create)


@when("User enters the mandatory details in the form")
def details():
    load_send_keys("id", Form.txt_f_name, Environment.f_name)
    load_send_keys("id", Form.txt_l_name, Environment.l_name)
    load_send_keys("id", Form.txt_password, Environment.password)
    load_send_keys("id", Form.txt_company, Environment.company)

    select_option_by_index(Form.ddl_days, random.randint(1, 30))
    select_option_by_index(Form.ddl_months, random.randint(1, 12))
    select_option_by_index(Form.ddl_years, random.randint(1, 10))

    load_send_keys("id", Form.txt_address_1, Environment.address_1)
    load_send_keys("id", Form.txt_city, Environment.city)
    select_option_by_index(Form.ddl_state, "3")
    load_send_keys("id", Form.txt_postcode, Environment.postcode)
    load_send_keys("id", Form.txt_mobile, Environment.mobile)
    wait_and_click("xpath", Form.btn_register)


@then("New Account is created")
def new_acc():
    wait_till_element_appears("xpath", Account.lbl_my_account)


@then("Name is appearing in the page")
def name_check():
    actual_name = driver.find_element_by_xpath(Account.lbl_acc_name).text
    expected_name = Environment.f_name + " " + Environment.l_name
    assert actual_name == expected_name
