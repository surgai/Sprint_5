from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from elements_to_find import TestLocators
@pytest.mark.usefixtures("chrome_browser")
class TestConstructor:
    def test_work_constructor(self):
#1 Проверим вход через кнопку Войти в аккаунт

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
# Ввод Email
        email = self.driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys('Nuykin_9@yandex.ru')
# Ввод Пароля
        password = self.driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys('qwerty123456')
# Нажми кнопку Войти
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(TestLocators.PUSH_ENTER_BUTTON)).click()

# Проверяю переход по клику на «Личный кабинет».
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(TestLocators.LK_BUTTON)).click()
# переход по клику на «Конструктор».
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(TestLocators.BUILD_BURGER_CLICK)).click()
#Проверяем работу конструктора - Булки Соусы Начинки
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(TestLocators.CONSTRUCTOR_SOUS)).click()
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.SCROL_TAB_TAB))).text == 'Соусы'
        self.driver.quit()