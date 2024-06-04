from selenium import webdriver
from elements_to_find import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
@pytest.mark.usefixtures("chrome_browser")
class TestAuthLogOut:
    def test_in_enter_account(self):
#1 Проверим вход через кнопку Войти в аккаунт
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
# Ввод Email
        email = self.driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys('Nuykin_9@yandex.ru')
# Ввод Пароля
        password = self.driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys('qwerty123456')
# Нажми кнопку Войти
        login = self.driver.find_element(*TestLocators.PUSH_ENTER_BUTTON)
        login.click()
# Проверяю переход по клику на «Личный кабинет».
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(TestLocators.LK_BUTTON_2)).click()

# Если на странице появилась кнопка Выход, значит авторизация успешна
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.EXIT_IN_LK_TEXT))).text == "Выход"
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((TestLocators.LOGOUT_BUTTON))).click()
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.ENTER_BUTTON_TEXT))).text == "Вход"
        self.driver.quit()
    def test_in_lk(self):
#2 Проверим авторизацию через кнопку Личный кабинет
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(*TestLocators.LK_BUTTON_2).click()
# Ввод Email
        email = self.driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys('Nuykin_9@yandex.ru')
# Ввод Пароля
        password = self.driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys('qwerty123456')
# Нажми кнопку Войти
        login = self.driver.find_element(*TestLocators.PUSH_ENTER_BUTTON)
        login.click()
# Проверяю переход по клику на «Личный кабинет».
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(TestLocators.LK_BUTTON_2)).click()

# Если на странице появилась кнопка Выход, значит авторизация успешна
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.EXIT_IN_LK_TEXT))).text == "Выход"
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((TestLocators.LOGOUT_BUTTON))).click()
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.ENTER_BUTTON_TEXT))).text == "Вход"
        self.driver.quit()
    def test_in_registration(self):
#3 Проверим авторизацию через кнопку в форме регистрации

        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(*TestLocators.REGISTRATION_REGISTRATION_BUTTON).click()
        self.driver.find_element(*TestLocators.ENTER_AFTER_RESET_PASS_LINK).click()
# Ввод Email
        email = self.driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys('Nuykin_9@yandex.ru')
# Ввод Пароля
        password = self.driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys('qwerty123456')
# Нажми кнопку Войти
        login = self.driver.find_element(*TestLocators.PUSH_ENTER_BUTTON)
        login.click()
#Проверяю переход по клику на «Личный кабинет».
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(TestLocators.LK_BUTTON_2)).click()

# Если на странице появилась кнопка Выход, значит авторизация успешна
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.EXIT_IN_LK_TEXT))).text == "Выход"
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((TestLocators.LOGOUT_BUTTON))).click()
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.ENTER_BUTTON_TEXT))).text == "Вход"
        self.driver.quit()
    def test_in_forgot_password_form(self):
# Вход через кнопку в форме восстановления пароля

        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(*TestLocators.TRASH_PASSWORD_BUTTON).click()
        self.driver.find_element(*TestLocators.PUSH_RESET_PASSWORD_TEXT).click()
        self.driver.find_element(*TestLocators.ENTER_AFTER_RESET_PASS_LINK).click()
# Ввод Email
        email = self.driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys('Nuykin_9@yandex.ru')
# Ввод Пароля
        password = self.driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys('qwerty123456')
# Нажми кнопку Войти
        login = self.driver.find_element(*TestLocators.PUSH_ENTER_BUTTON)
        login.click()
# Проверяю переход по клику на «Личный кабинет».
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(TestLocators.LK_BUTTON_2)).click()

# Если на странице появилась кнопка Выход, значит авторизация успешна
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.EXIT_IN_LK_TEXT))).text == "Выход"
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((TestLocators.LOGOUT_BUTTON))).click()
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.ENTER_BUTTON_TEXT))).text == "Вход"
        self.driver.quit()