from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from elements_to_find import TestLocators

class TestAuthLogOut:
    def test_in_enter_account(self):
#1 Проверим вход через кнопку Войти в аккаунт
        driver = webdriver.Chrome()
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
# Если на странице появилась кнопка Выход, значит авторизация успешна
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.EXIT_IN_LK_TEXT)
        except NoSuchElementException:
            print("Вход выполняется через кнопку 'Войти в аккаунт': Вы не авторизованы в системе ")
        else:
            print("Вход выполняется через кнопку 'Войти в аккаунт': Авторизация успешно выполнена")

        driver.implicitly_wait(5)
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.ENTER_BUTTON_TEXT)
            driver.implicitly_wait(5)
        except NoSuchElementException:
            print("Вы не разлогинилсь")
        else:
            print("Вы успешно разлогинились")

        driver.quit()
    def test_in_lk(self):
#2 Проверим авторизацию через кнопку Личный кабинет
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.LK_BUTTON).click()
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
# Если на странице появилась кнопка Выход, значит авторизация успешна
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.EXIT_IN_LK_TEXT)
        except NoSuchElementException:
            print("Вход выполняется через 'Личный кабиент': Вы не авторизованы в системе")
        else:
            print("Вход выполняется через 'Личный кабиент': Авторизация успешно выполнена")
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.ENTER_BUTTON_TEXT)
            driver.implicitly_wait(5)
        except NoSuchElementException:
            print("Вы не разлогинилсь")
        else:
            print("Вы успешно разлогинились")
        driver.quit()
    def test_in_registration(self):
#3 Проверим авторизацию через кнопку в форме регистрации
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.REGISTRATION_REGISTRATION_BUTTON).click()
        driver.find_element(*TestLocators.ENTER_AFTER_RESET_PASS_LINK).click()
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
#Проверяю переход по клику на «Личный кабинет».
        driver.find_element(*TestLocators.LK_BUTTON).click()

# Если на странице появилась кнопка Выход, значит авторизация успешна
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.EXIT_IN_LK_TEXT)
        except NoSuchElementException:
            print("Вход выполняется через форму регистрации: Вы не авторизованы в системе")
        else:
            print("Вход выполняется через форму регистрации: Авторизация успешно выполнена")
        driver.implicitly_wait(5)
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.ENTER_BUTTON_TEXT)
            driver.implicitly_wait(5)
        except NoSuchElementException:
            print("Вы не разлогинилсь")
        else:
            print("Вы успешно разлогинились")
        driver.quit()
    def test_in_forgot_password_form(self):
# Вход через кнопку в форме восстановления пароля

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.TRASH_PASSWORD_BUTTON).click()
        driver.find_element(*TestLocators.PUSH_RESET_PASSWORD_TEXT).click()
        driver.implicitly_wait(5)
        driver.find_element(*TestLocators.ENTER_AFTER_RESET_PASS_LINK).click()
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
# Если на странице появилась кнопка Выход, значит авторизация успешна
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.EXIT_IN_LK_TEXT)
        except NoSuchElementException:
            print("Вход выполняется через форму восстановления пароля: Вы не авторизованы в системе")
        else:
            print("Вход выполняется через форму восстановления пароля: Авторизация успешно выполнена")
        driver.implicitly_wait(5)
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        try:
            driver.implicitly_wait(5)
            driver.find_element(*TestLocators.ENTER_BUTTON_TEXT)
            driver.implicitly_wait(5)
        except NoSuchElementException:
            print("Вы не разлогинилсь")
        else:
            print("Вы успешно разлогинились")
        driver.quit()