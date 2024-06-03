from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from elements_to_find import TestLocators


class TestConstructor:
    def test_work_constructor(self):
#1 Проверим вход через кнопку Войти в аккаунт
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(5)
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
        time.sleep(5)
# Проверяю переход по клику на «Личный кабинет».
        driver.find_element(*TestLocators.LK_BUTTON).click()
# переход по клику на «Конструктор».
        time.sleep(5)
        driver.find_element(*TestLocators.BUILD_BURGER_CLICK).click()
#Проверяем работу конструктора - Булки Соусы Начинки
        time.sleep(5)
        driver.find_element(*TestLocators.CONSTRUCTOR_SOUS).click()
        assert WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.SCROL_TAB_TAB))).text == 'Соусы'
        time.sleep(5)
        driver.find_element(*TestLocators.CONSTRUCTOR_NACHINKI).click()
        assert WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.SCROL_TAB_TAB))).text == 'Начинки'
        time.sleep(5)
        driver.find_element(*TestLocators.CONSTRUCTOR_BULKI).click()
        time.sleep(5)
        assert WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.SCROL_TAB_TAB))).text == 'Булки'
        driver.quit()
