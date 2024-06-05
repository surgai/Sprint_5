import pytest
from elements_to_find import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
@pytest.mark.usefixtures("chrome_browser")
class TestEnterConstructor:
    def test_enter_constructor(self):
#1 Проверим вход через кнопку Войти в аккаунт

        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
# Ввод Email
        email = self.driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys('Nuykin_9@yandex.ru')
# Ввод Пароля
        password = self.driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys('qwerty1234561')
# Нажми кнопку Войти
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(TestLocators.PUSH_ENTER_BUTTON)).click()

# Проверяю переход по клику на «Личный кабинет».
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(TestLocators.LK_BUTTON)).click()
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(TestLocators.BUILD_BURGER_CLICK)).click()
        assert WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((TestLocators.TEST_BURGER))).text == "Соберите бургер"
