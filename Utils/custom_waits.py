from Drivers.browser import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

wait = WebDriverWait(driver, 20)


def wait_till_element_appears(locator_type, element):
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

    element_text_field.clear()
    element_text_field.send_keys(key)


def select_option_by_index(element, index):
    dropdown = Select(driver.find_element_by_id(element))
    dropdown.select_by_index(index)


#Get the text inside the tag "<span>this is text</span>"
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
