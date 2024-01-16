import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#comment moment
@pytest.fixture()
def browser():
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    # browser.maximize_window()
    yield browser
    time.sleep(3)
    browser.quit()

