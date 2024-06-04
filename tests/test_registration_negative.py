from selenium import webdriver
import re
import secrets
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import TestLocators
import pytest
@pytest.mark.usefixtures("chrome_browser")
class TestRegistration:
    def test_registration(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        assert "stellarburgers.nomoreparties.site" in self.driver.current_url
# Найди поле "Имя" и заполни его
        alphabet = string.ascii_letters + string.digits
        passw = ''.join(secrets.choice(alphabet) for i in range(3))
        login = f"Nuykin_9_{passw}@ya.ru"
        name = self.driver.find_element(*TestLocators.NAME_REGISTRATION_FIELD)
        name.send_keys("Денис")
        assert name.get_attribute('value') != ''
# Найди поле "Email" и заполни его
        email = self.driver.find_element(*TestLocators.EMAIL_REGISTRATION_FIELD)
        email.send_keys(login)
        assert re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)', email.get_attribute('value'))
# Найди поле "Пароль" и заполни его
        password = self.driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FIELD)
        password.send_keys(passw)
# Нажми кнопку Зарегистрироваться
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((TestLocators.REGISTRATION_REGISTRATION_BUTTON))).click()
#при неверном пароле проверяю что есть предупреждение с текстом Некорректный пароль

        attention = WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((TestLocators.WRONGPASS_REGISTARTION_TEXT))).text
        assert attention == 'Некорректный пароль'
        self.driver.quit()