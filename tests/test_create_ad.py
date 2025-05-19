from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import AuthLocators, SignupLocators, PostAdLocators
from factory_helpers import make_email, make_password
from conftest import *


class TestCreateAd:

    def test_authorized_user_can_create_ad(self, driver, registered_user):
        driver.get(URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(PostAdLocators.BTN_NEW_AD)).click()

        wait.until(EC.visibility_of_element_located(PostAdLocators.FIELD_TITLE)).send_keys("Гитара")
        driver.find_element(*PostAdLocators.FIELD_PRICE).send_keys("10000")

        driver.find_element(*PostAdLocators.DROPDOWN_CATEGORY).click()
        wait.until(EC.element_to_be_clickable(PostAdLocators.SELECT_CATEGORY)).click()

        driver.find_element(*PostAdLocators.DROPDOWN_CITY).click()
        wait.until(EC.element_to_be_clickable(PostAdLocators.SELECT_CITY)).click()

        driver.find_element(*PostAdLocators.RADIO_CONDITION_NEW).click()

        driver.find_element(*PostAdLocators.BTN_PUBLISH).click()

        wait.until(EC.visibility_of_element_located(PostAdLocators.SECTION_MY_ADS))
        ad_title = wait.until(EC.visibility_of_element_located(PostAdLocators.ITEM_AD)).text
        ad_price = wait.until(EC.visibility_of_element_located(PostAdLocators.ITEM_AD)).text
        ad_city = wait.until(EC.visibility_of_element_located(PostAdLocators.ITEM_AD)).text

        assert ad_title == "Гитара"
        assert ad_price == "10 000 ₽"
        assert ad_city == "Москва"
