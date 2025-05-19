import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from factory_helpers import make_email, make_password
from urls import URL
from data import Login_Test




@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.fixture()
def logged_in_user(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)

    wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
    wait.until(EC.visibility_of_element_located(AuthLocators.INPUT_EMAIL)).send_keys(Login_Test.EXISTING_USER_EMAIL)
    driver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(Login_Test.EXISTING_USER_PASSWORD)
    driver.find_element(*AuthLocators.BTN_SUBMIT_LOGIN).click()

    wait.until(EC.visibility_of_element_located(AuthLocators.NAME_USER))
    return {"email": Login_Test.EXISTING_USER_EMAIL}

@pytest.fixture
def registered_user(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)

    email = make_email()
    password = make_password()

    wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
    wait.until(EC.element_to_be_clickable(SignupLocators.BTN_NO_ACCOUNT)).click()
    wait.until(EC.visibility_of_element_located(SignupLocators.INPUT_EMAIL)).send_keys(email)
    driver.find_element(*SignupLocators.INPUT_PASS).send_keys(password)
    driver.find_element(*SignupLocators.INPUT_PASS_CONFIRM).send_keys(password)
    driver.find_element(*SignupLocators.BTN_CREATE_ACCOUNT).click()

    wait.until(EC.visibility_of_element_located(AuthLocators.NAME_USER))

    return {"email": email, "password": password}