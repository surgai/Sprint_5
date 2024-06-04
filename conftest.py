
import pytest
from selenium import webdriver

@pytest.fixture
def chrome_browser(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()