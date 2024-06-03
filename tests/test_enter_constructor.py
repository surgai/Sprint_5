import time
from selenium import webdriver
from elements_to_find import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
class TestConstructor:
    def test_enter_constructor(self):
#1 Проверим вход через кнопку Войти в аккаунт
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
# Ввод Email
        email = driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys('Nuykin_9@yandex.ru')
# Ввод Пароля
        password = driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys('qwerty1234561')
# Нажми кнопку Войти
        login = driver.find_element(*TestLocators.PUSH_ENTER_BUTTON)
        login.click()

# Проверяю переход по клику на «Личный кабинет».
        driver.find_element(*TestLocators.LK_BUTTON).click()
        time.sleep(3)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(TestLocators.LK_BUTTON)).click()
        time.sleep(3)
#        driver.find_element(*TestLocators.BUILD_BURGER_CLICK).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(TestLocators.BUILD_BURGER_CLICK)).click()
        time.sleep(3)
        assert driver.find_element(*TestLocators.TEST_BURGER).text == "Соберите бургер"
        driver.quit()