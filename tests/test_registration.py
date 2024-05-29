import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from elements_to_find import TestLocators
import re

@pytest.mark.usefixtures("generate_data")
class TestRegistration:
    def test_registration(self):
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        driver.get("https://stellarburgers.nomoreparties.site/register")

# Найди поле "Имя" и заполни его
        name = driver.find_element(*TestLocators.NAME_REGISTRATION_FIELD)
        name.send_keys("Денис")
        assert name.get_attribute('value') != ''

# Найди поле "Email" и заполни его
        email = driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys(self.login)
        assert re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email.get_attribute('value'))

# Найди поле "Пароль" и заполни его
        password = driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys(self.password)
        assert len(password.get_attribute('value')) > 5

# Нажми кнопку Зарегистрироваться
        registration = driver.find_element(*TestLocators.REGISTRATION_REGISTRATION_BUTTON)
        registration.click()
#Проверка валидности введенного пароля и  наличия пользователя в системе
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.WRONGPASS_REGISTARTION_TEXT)
        except NoSuchElementException:
            print("Пароль валидный")
        else:
            print("Пароль не валидный")

        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.EXISTUSER_REGISTRATION_TEXT)
        except NoSuchElementException:
            print("Регистрация выполнена")
        else:
            print("Такой пользователь уже существует")

        driver.quit()