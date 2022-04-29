from Drivers.browser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

wait = WebDriverWait(driver, 20)


def wait_till_element_disappears(locator_type, element):
    if locator_type == "id":
        wait.until(EC.invisibility_of_element_located((By.ID, element)))
    elif locator_type == "xpath":
        wait.until(EC.invisibility_of_element_located((By.XPATH, element)))
    elif locator_type == "css":
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, element)))
    elif locator_type == "class":
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, element)))


def wait_till_element_appears(locator_type, element, polling_interval):
    if locator_type == "id":
        wait.until(EC.visibility_of_element_located((By.ID, element)))
    elif locator_type == "xpath":
        wait.until(EC.visibility_of_element_located((By.XPATH, element)))
    elif locator_type == "css":
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
    elif locator_type == "name":
        wait.until(EC.visibility_of_element_located((By.NAME, element)))
    elif locator_type == "class":
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, element)))


def wait_till_element_present(locator_type, element):
    if locator_type == "id":
        wait.until(EC.presence_of_element_located((By.ID, element)))
    elif locator_type == "xpath":
        wait.until(EC.presence_of_element_located((By.XPATH, element)))
    elif locator_type == "css":
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
    elif locator_type == "name":
        wait.until(EC.presence_of_element_located((By.NAME, element)))
    elif locator_type == "class":
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, element)))


def wait_and_click(locator_type, element):
    if locator_type == "id":
        wait.until(EC.element_to_be_clickable((By.ID, element))).click()
    elif locator_type == "xpath":
        wait.until(EC.element_to_be_clickable((By.XPATH, element))).click()
    elif locator_type == "css":
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element))).click()
    elif locator_type == "name":
        wait.until(EC.element_to_be_clickable((By.NAME, element))).click()
    elif locator_type == "class":
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, element))).click()
    elif locator_type == "linkText":
        wait.until(EC.element_to_be_clickable(By.LINK_TEXT, element)).click()


def mouse_hover_and_click(locator_type, element):
    action = ActionChains(driver)
    if locator_type == "id":
        ele = wait.until(EC.presence_of_element_located((By.ID, element)))
    elif locator_type == "xpath":
        ele = wait.until(EC.presence_of_element_located((By.XPATH, element)))
    elif locator_type == "css":
        ele = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
    elif locator_type == "name":
        ele = wait.until(EC.presence_of_element_located((By.NAME, element)))
    elif locator_type == "class":
        ele = wait.until(EC.presence_of_element_located((By.CLASS_NAME, element)))

    action.move_to_element(ele).click().perform()


def wait_till_frame_displayed(locator_type, element):
    if locator_type == "id":
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, element)))
    elif locator_type == "xpath":
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, element)))
    elif locator_type == "css":
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, element)))


def wait_if_displayed(locator_type, element, wait_time):
    count = 0
    interval = 0.1
    total_wait = wait_time / interval
    if locator_type == "id":
        while (len(driver.find_elements_by_id(element)) == 0):
            time.sleep(interval)
            count = count + 1
            if (count == total_wait):
                break
    elif locator_type == "xpath":
        while (len(driver.find_elements_by_xpath(element)) == 0):
            time.sleep(interval)
            count = count + 1
            if (count == total_wait):
                break
    elif locator_type == "css":
        while (len(driver.find_elements_by_css_selector(element)) == 0):
            time.sleep(interval)
            count = count + 1
            if (count == total_wait):
                break


def load_send_keys(locator_type, element, key):
    if locator_type == "id":
        element_text_field = wait.until(EC.visibility_of_element_located((By.ID, element)))
    elif locator_type == "xpath":
        element_text_field = wait.until(EC.visibility_of_element_located((By.XPATH, element)))
    elif locator_type == "css":
        element_text_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
    elif locator_type == "name":
        element_text_field = wait.until(EC.visibility_of_element_located((By.NAME, element)))
    elif locator_type == "class":
        element_text_field = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, element)))

    if (element_text_field.is_enabled()):
        # Delete the existing data using Backspace key
        # We can User either element_text_field.clear() instead
        # element_text_field.send_keys(Keys.BACK_SPACE * len(get_text(locator_type, element)))
        if (element_text_field.tag_name == 'input' and (len(get_attribute_value(locator_type, element, 'value')) > 0)):
            element_text_field.clear()
        else:
            element_text_field.send_keys(Keys.BACK_SPACE * len(get_text(locator_type, element)))
        element_text_field.send_keys(key)


# Get the text inside the tag "<p>this is text</p>"
def get_text(locator_type, element):
    if locator_type == "id":
        text = wait.until(EC.presence_of_element_located((By.ID, element))).text
    elif locator_type == "xpath":
        text = wait.until(EC.presence_of_element_located((By.XPATH, element))).text
    elif locator_type == "css":
        text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element))).text
    elif locator_type == "name":
        text = wait.until(EC.presence_of_element_located((By.NAME, element))).text
    elif locator_type == "class":
        text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, element))).text
    return text


# To get the value with selenium element.get_attribute('value')
def get_attribute_value(locator_type, element, attribute_name):
    if locator_type == "id":
        value = wait.until(EC.presence_of_element_located((By.ID, element))).get_attribute(attribute_name)
    elif locator_type == "xpath":
        value = wait.until(EC.presence_of_element_located((By.XPATH, element))).get_attribute(attribute_name)
    elif locator_type == "css":
        value = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element))).get_attribute(attribute_name)
    elif locator_type == "name":
        value = wait.until(EC.presence_of_element_located((By.NAME, element))).get_attribute(attribute_name)
    elif locator_type == "class":
        value = wait.until(EC.presence_of_element_located((By.CLASS_NAME, element))).get_attribute(attribute_name)
    return value


# To Get the checkbox status
def is_checked(locator_type, element):
    if locator_type == "xpath":
        status = wait.until(EC.presence_of_element_located((By.XPATH, element))).is_selected()
    return status


# wait until the url is reached
def wait_until_url(url):
    wait.until(EC.url_to_be(url))