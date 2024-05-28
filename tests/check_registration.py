
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from elements_to_find import TestLocators
import re


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

# Найди поле "Имя" и заполни его
name = driver.find_element(*TestLocators.NAME_REGISTRATION_FIELD)
name.send_keys('Денис')
assert name.get_attribute('value') != ''

# Найди поле "Email" и заполни его
email = driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
email.send_keys('Nuykin_9@yandex.ru')
assert re.match('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',email.get_attribute('value'))

# Найди поле "Пароль" и заполни его
password = driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
password.send_keys('qwerty123456')
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