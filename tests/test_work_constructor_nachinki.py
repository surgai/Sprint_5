
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from elements_to_find import TestLocators
@pytest.mark.usefixtures("chrome_browser")

class TestConstructor:
    def test_work_constructor(self):
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
        self.driver.find_element(*TestLocators.PUSH_ENTER_BUTTON).click()
# Проверяю переход по клику на «Личный кабинет».
        self.driver.find_element(*TestLocators.LK_BUTTON).click()
# переход по клику на «Конструктор».
        self.driver.find_element(*TestLocators.BUILD_BURGER_CLICK).click()
#Проверяем работу конструктора - Булки Соусы Начинки
        self.driver.find_element(*TestLocators.CONSTRUCTOR_NACHINKI).click()
        assert WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.SCROL_TAB_TAB))).text == 'Начинки'

