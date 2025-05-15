# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from locators import AuthLocators, SignupLocators
from factory_helpers import make_email, make_password
from urls import URL
from data import Invalid_email_shows_error
from conftest import *


class TestRegistration:

    def test_can_register_with_valid_data(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(URL)

        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
        wait.until(EC.element_to_be_clickable(SignupLocators.BTN_NO_ACCOUNT)).click()

        email = make_email()
        password = make_password()

        wait.until(EC.visibility_of_element_located(SignupLocators.INPUT_EMAIL)).send_keys(email)
        driver.find_element(*SignupLocators.INPUT_PASS).send_keys(password)
        driver.find_element(*SignupLocators.INPUT_PASS_CONFIRM).send_keys(password)
        driver.find_element(*SignupLocators.BTN_CREATE_ACCOUNT).click()

        user_name = wait.until(EC.visibility_of_element_located(AuthLocators.NAME_USER)).text
        assert user_name.rstrip('.') == "User"

    def test_registration_with_invalid_email_shows_error(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(URL)

        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
        wait.until(EC.element_to_be_clickable(SignupLocators.BTN_NO_ACCOUNT)).click()

        driver.find_element(*SignupLocators.INPUT_EMAIL).send_keys(Invalid_email_shows_error.INVALID_MAIL)
        driver.find_element(*SignupLocators.INPUT_PASS).send_keys(Invalid_email_shows_error.INVALID_PASS)
        driver.find_element(*SignupLocators.INPUT_PASS_CONFIRM).send_keys(Invalid_email_shows_error.CONFIRM_INVALID_PASS)
        driver.find_element(*SignupLocators.BTN_CREATE_ACCOUNT).click()

        # Проверка появления сообщения об ошибке
        error_label = wait.until(EC.visibility_of_element_located(SignupLocators.LABEL_ERROR))
        assert error_label.text.strip() == "Ошибка"

    def test_password_mismatch_shows_error(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(URL)

        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
        wait.until(EC.element_to_be_clickable(SignupLocators.BTN_NO_ACCOUNT)).click()

        email = make_email()

        wait.until(EC.visibility_of_element_located(SignupLocators.INPUT_EMAIL)).send_keys(email)
        driver.find_element(*SignupLocators.INPUT_PASS).send_keys("Password123")
        driver.find_element(*SignupLocators.INPUT_PASS_CONFIRM).send_keys("WrongPassword123")
        driver.find_element(*SignupLocators.BTN_CREATE_ACCOUNT).click()

        # Явное сообщение "Пароли не совпадают"
        error = wait.until(EC.visibility_of_element_located(AuthLocators.EXPLICIT_MESSAGE))

        assert "Пароли не совпадают" in error.text

    def test_register_existing_user_shows_error(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(URL)

        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
        wait.until(EC.element_to_be_clickable(SignupLocators.BTN_NO_ACCOUNT)).click()

        # Этот email уже был использован ранее
        email = "existing_user@test.com"
        password = "TestPassword123"

        wait.until(EC.visibility_of_element_located(SignupLocators.INPUT_EMAIL)).send_keys(email)
        driver.find_element(*SignupLocators.INPUT_PASS).send_keys(password)
        driver.find_element(*SignupLocators.INPUT_PASS_CONFIRM).send_keys(password)
        driver.find_element(*SignupLocators.BTN_CREATE_ACCOUNT).click()

        # Ожидаем сообщение "Ошибка"
        error_label = wait.until(EC.visibility_of_element_located(SignupLocators.LABEL_ERROR))
        assert error_label.text.strip() == "Ошибка"

