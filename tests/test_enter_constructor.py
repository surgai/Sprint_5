from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from elements_to_find import TestLocators

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
        driver.implicitly_wait(5)
# Проверяю переход по клику на «Личный кабинет».
        driver.find_element(*TestLocators.LK_BUTTON).click()
# Если на странице появилась кнопка Выход, значит авторизация успешна
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.EXIT_IN_LK_TEXT)
        except NoSuchElementException:
            print("Вход выполняется через кнопку 'Войти в аккаунт': Вы не авторизованы в системе ")
        else:
            print("Вход выполняется через кнопку 'Войти в аккаунт': Авторизация успешно выполнена")
# Проверяю что кнопка Конструктор есть и после перехода на нее на странице отображается элемент "Соберите бургер"
        driver.find_element(*TestLocators.BUILD_BURGER_CLICK).click()
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.BUILD_BURGER_TEXT)
            driver.implicitly_wait(5)
        except NoSuchElementException:
            print("Страница Конструктор в Личном кабинете обнаружена, после перехода видим меню конструктора Соберите бургер")
        else:
            print("Вход в на страницу Конструктор не выполнен")
#driver.implicitly_wait(5)
#driver.find_element(*TestLocators.STELLA_BURGER_LINK).click()
        driver.quit()