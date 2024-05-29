from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from elements_to_find import TestLocators

#1 Проверим вход через кнопку Войти в аккаунт
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920,1080')

driver.get("https://stellarburgers.nomoreparties.site")
driver.implicitly_wait(5)
driver.get("https://stellarburgers.nomoreparties.site")
driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
# Ввод Email
email = driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
email.send_keys('Nuykin_9@yandex.ru')
# Ввод Пароля
password = driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
password.send_keys('qwerty123456')
# Нажми кнопку Войти
login = driver.find_element(*TestLocators.PUSH_ENTER_BUTTON)
login.click()
driver.implicitly_wait(5)
# Проверяю переход по клику на «Личный кабинет».
driver.find_element(*TestLocators.LK_BUTTON).click()

# переход по клику на «Конструктор».
driver.implicitly_wait(5)
driver.find_element(*TestLocators.CONSTRUCTOR_CLICK).click()

#Проверяем работу конструктора - Булки Соусы Начинки
driver.implicitly_wait(5)
driver.find_element(*TestLocators.CONSTRUCTOR_SOUS).click()
driver.implicitly_wait(5)
driver.find_element(*TestLocators.CONSTRUCTOR_NACHINKI).click()
driver.implicitly_wait(5)
driver.find_element(*TestLocators.CONSTRUCTOR_BULKI).click()
driver.implicitly_wait(5)
driver.quit()
