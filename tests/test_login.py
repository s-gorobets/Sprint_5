from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data import EXISTING_USER_PASSWORD, EXISTING_USER_EMAIL
from locators import *
from conftest import *

class TestLogin:
    def test_user_can_login_with_valid_credentials(self, driver):
        # Открываем сайт
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
        wait.until(EC.element_to_be_clickable(SignupLocators.BTN_NO_ACCOUNT)).click()
        wait.until(EC.visibility_of_element_located(SignupLocators.INPUT_EMAIL)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*SignupLocators.INPUT_PASS).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*SignupLocators.INPUT_PASS_CONFIRM).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*SignupLocators.BTN_CREATE_ACCOUNT).click()

        # Проверяем, что вошли
        name = wait.until(EC.visibility_of_element_located(AuthLocators.NAME_USER)).text
        assert name.rstrip('.') == "User"

        # Logout
        wait.until(EC.visibility_of_element_located(AuthLocators.ICON_USER)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_OUT)).click()

        # Login с теми же данными
        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.INPUT_EMAIL)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*AuthLocators.INPUT_PASSWORD).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthLocators.BTN_SUBMIT_LOGIN).click()

        # Проверяем снова имя
        name_after_login = wait.until(EC.visibility_of_element_located(AuthLocators.NAME_USER)).text
        assert name_after_login.rstrip('.') == "User"