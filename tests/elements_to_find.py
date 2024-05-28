from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLocators:
    NAME_REGISTRATION_FIELD = By.XPATH, ".//*[text()='Имя']/following-sibling::input"
    EMAIL_REGISTRATION_FIELD = By.XPATH, ".//*[text()='Email']/following-sibling::input"
    PASSWORD_REGISTRATION_FIELD = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"
    REGISTRATION_REGISTRATION_BUTTON = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    WRONGPASS_REGISTARTION_TEXT = By.XPATH, "//*[contains(text(), 'Некорректный пароль')]"
    EXISTUSER_REGISTRATION_TEXT = By.XPATH, "//*[contains(text(), 'Такой пользователь уже существует')]"

    ENTER_TO_ACCOUNT_BUTTON = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    PUSH_ENTER_BUTTON = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    LK_BUTTON = By.XPATH, "/html/body/div/div/header/nav/a/p"
    EXIT_IN_LK_TEXT = By.XPATH, ".//*[contains(text(), 'Выход')]"
    TRASH_PASSWORD_BUTTON = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    PUSH_RESET_PASSWORD_TEXT = By.LINK_TEXT, "Восстановить пароль"
    ENTER_AFTER_RESET_PASS_LINK = By.LINK_TEXT, "Войти"
    LK_IN_MAIN_BUTTON = By.XPATH, "/html/body/div/div/header/nav/a/p"
    BUILD_BURGER_CLICK = By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p"
    BUILD_BURGER_TEXT = By.XPATH, "text.text_type_main-large.mb-5.mt-10"
    STELLA_BURGER_LINK = By.XPATH, "/html/head/link[3]"

    LOGOUT_BUTTON = By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button"
    ENTER_BUTTON_TEXT = By.XPATH, "//*[contains(text(), 'Вход')]"
    CONSTRUCTOR_CLICK = By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p"
    CONSTRUCTOR_BULKI = By.XPATH, ".//*[contains(text(), 'Булки')]"
    CONSTRUCTOR_SOUS = By.XPATH, ".//*[contains(text(), 'Соусы')]"
    CONSTRUCTOR_NACHINKI = By.XPATH, ".//*[contains(text(), 'Начинки')]"