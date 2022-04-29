from selenium.webdriver.support.select import Select
import time
import random
import requests
import json
from Drivers.browser import driver
from Utils.custom_waits import wait_and_click, wait_till_element_appears


class Actions:
    def dropdown(self, dropdown, element):
        wait_till_element_appears("id", dropdown, 0.1)
        try:
            select = Select(driver.find_element_by_id(dropdown))
            select.select_by_index(random.randint(1,12))
        except:
            time.sleep(2)
            select = Select(driver.find_element_by_id(dropdown))
            select.select_by_index(random.randint(1,12))

    def switch_tab(tab_num,action):
        if action == 'open':
            driver.execute_script("window.open('');")
            # Switch to the new window
            driver.switch_to.window(driver.window_handles[tab_num])
        elif action == 'close':
            driver.switch_to.window(driver.window_handles[tab_num])
            driver.close()
        elif action == 'switch':
            driver.switch_to.window(driver.window_handles[tab_num])
    driver.switch_to.default_content()

class Name_Generator:
    def Name(self):
        return(str(time.time()))


name = Name_Generator()

class Environment:
    url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    email = "vishnu"+name.Name()+"@sasi.com"
    f_name = "Vishnu"
    l_name = "M J"
    password = "passwd"
    company = "SurveySparrow"
    address_1 = "Infopark Phase 2"
    city = "Kochi"
    state = "Kentucky"
    postcode = "00000"
    country = "India"
    mobile = "8714457241"
