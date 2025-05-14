from selenium.webdriver.common.by import By

class AuthLocators:
    BTN_SIGN_IN = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and contains(text(), 'Вход и регистрация')]")
    INPUT_EMAIL = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Введите Email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Пароль']")
    BTN_SUBMIT_LOGIN = (By.XPATH, "//button[text()='Войти']")
    ICON_USER = (By.XPATH, "//*[contains(@class, 'svgSmall')]")
    NAME_USER = (By.XPATH, "//h3[contains(@class, 'profileText name')]")
    BTN_SIGN_OUT = (By.XPATH, "//button[text()='Выйти']")
    BTN_PROFILE = (By.XPATH, "//button[contains(@class, 'circleSmall')]")

class SignupLocators:
    BTN_NO_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    INPUT_EMAIL = AuthLocators.INPUT_EMAIL
    INPUT_PASS = AuthLocators.INPUT_PASSWORD
    INPUT_PASS_CONFIRM = (By.XPATH, "//input[@placeholder='Повторите пароль']")
    BTN_CREATE_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")

    # Ошибки валидации
    LABEL_ERROR = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")
    EMAIL_ERROR_FIELD = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(1) .input_invalid")
    PASS_ERROR_FIELD = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(2) .input_invalid")
    CONFIRM_ERROR_FIELD = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(3) .input_invalid")

class PostAdLocators:
    BTN_NEW_AD = (By.XPATH, "//button[text()='Разместить объявление']")
    FIELD_TITLE = (By.XPATH, "//input[@placeholder='Название']")
    FIELD_PRICE = (By.CSS_SELECTOR, "input[name='price']")
    DROPDOWN_CATEGORY = (By.XPATH, ".//button[contains(@class, 'dropDownMenu_arrowDown')]")
    SELECT_CATEGORY = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw input[name='category']")
    DROPDOWN_CITY = (By.XPATH, "//input[@name='city']/following-sibling::button")
    SELECT_CITY = (By.CSS_SELECTOR, "div.dropDownMenu_input__itKtw input[name='city']")
    RADIO_CONDITION_NEW = (By.XPATH, "//label[text()='Новый']")
    BTN_PUBLISH = (By.XPATH, "//button[text()='Опубликовать']")
    SECTION_MY_ADS = (By.XPATH, "//h1[text()='Мои объявления']")
    ITEM_AD = (By.XPATH, "//div[contains(@class, 'description')]")
    MODAL_SIGN_IN_PROMPT = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

