# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from locators import AuthLocators, SignupLocators
from factory_helpers import make_email, make_password
from urls import URL
from conftest import *


class TestLogout:
    def test_user_can_logout_after_registration(self, driver, logged_in_user):
        driver.get(URL)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_PROFILE)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.BTN_SIGN_OUT)).click()
        assert wait.until(EC.visibility_of_element_located(AuthLocators.BTN_SIGN_IN)).is_displayed()

