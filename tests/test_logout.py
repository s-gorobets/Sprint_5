from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, SignupLocators
from factory_helpers import make_email, make_password
from conftest import *


class TestLogout:
    def test_user_can_logout_after_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        wait = WebDriverWait(driver, 5)

        email = make_email()
        password = make_password()

        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
        wait.until(EC.element_to_be_clickable(SignupLocators.BTN_NO_ACCOUNT)).click()
        wait.until(EC.visibility_of_element_located(SignupLocators.INPUT_EMAIL)).send_keys(email)
        driver.find_element(*SignupLocators.INPUT_PASS).send_keys(password)
        driver.find_element(*SignupLocators.INPUT_PASS_CONFIRM).send_keys(password)
        driver.find_element(*SignupLocators.BTN_CREATE_ACCOUNT).click()

        user_name = wait.until(EC.visibility_of_element_located(AuthLocators.NAME_USER)).text
        assert user_name.rstrip('.') == "User"

        wait.until(EC.element_to_be_clickable(AuthLocators.ICON_USER)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_OUT)).click()

        sign_in_btn = wait.until(EC.visibility_of_element_located(AuthLocators.BTN_SIGN_IN))
        assert sign_in_btn.is_displayed()
