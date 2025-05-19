# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from data import Login_Test
from urls import URL
# from locators import *
from conftest import *

class TestLogin:
    def test_user_can_login_with_valid_credentials(self, driver):
        # Открываем сайт
        driver.get(URL)
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_IN)).click()
        wait.until(EC.element_to_be_clickable(SignupLocators.BTN_NO_ACCOUNT)).click()
        wait.until(EC.visibility_of_element_located(SignupLocators.INPUT_EMAIL)).send_keys(Login_Test.EXISTING_USER_EMAIL)
        driver.find_element(*SignupLocators.INPUT_PASS).send_keys(Login_Test.EXISTING_USER_PASSWORD)
        driver.find_element(*SignupLocators.INPUT_PASS_CONFIRM).send_keys(Login_Test.EXISTING_USER_PASSWORD)
        driver.find_element(*SignupLocators.BTN_CREATE_ACCOUNT).click()

        # Проверяем, что вошли
        name = wait.until(EC.visibility_of_element_located(AuthLocators.NAME_USER)).text
        assert name.rstrip('.') == "User"