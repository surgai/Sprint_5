from selenium import webdriver
import time
from elements_to_find import TestLocators
import re
import secrets
import string

class TestRegistration():
    def test_registration(self):
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        driver.get("https://stellarburgers.nomoreparties.site/register")
        assert "stellarburgers.nomoreparties.site" in driver.current_url

# Найди поле "Имя" и заполни его

        alphabet = string.ascii_letters + string.digits
        passw = ''.join(secrets.choice(alphabet) for i in range(6))
        login = f"Nuykin_9_{passw}@ya.ru"
        name = driver.find_element(*TestLocators.NAME_REGISTRATION_FIELD)
        name.send_keys("Денис")
        assert name.get_attribute('value') != ''

# Найди поле "Email" и заполни его
        email = driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys(login)
        assert re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email.get_attribute('value'))

# Найди поле "Пароль" и заполни его
        password = driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys(passw)

# Нажми кнопку Зарегистрироваться
        registration = driver.find_element(*TestLocators.REGISTRATION_REGISTRATION_BUTTON)
        registration.click()

#при неверном пароле проверяю что есть предупреждение с текстом Некорректный пароль
        time.sleep(5)
        enter_button = driver.find_element(*TestLocators.ЕNTER_AFTER_REG).text
        assert enter_button == 'Войти'
        driver.quit()