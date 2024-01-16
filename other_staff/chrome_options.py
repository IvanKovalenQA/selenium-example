import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Создание объекта опций Chrome
chrome_options = Options()
chrome_options.add_argument("--lang=en")


# Создание объекта сервиса ChromeDriver
driver_service = Service(ChromeDriverManager().install())

# Создание экземпляра Chrome WebDriver с указанными опциями и сервисом
driver = webdriver.Chrome(service=driver_service, options=chrome_options)



# Дальнейшие действия с WebDriver...
driver.get("https://www.google.com/")
assert 'Google' == driver.title
driver.find_element(By.NAME, "q").send_keys("Macbook Pro" + Keys.ENTER)
assert 'Macbook Pro - Google Search' == driver.title
time.sleep(5)
# Закрытие браузера и завершение работы WebDriver
driver.quit()
