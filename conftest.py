
import pytest
from selenium import webdriver

@pytest.fixture
def chrome_browser(request):
    driver = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    request.cls.driver = driver

    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()