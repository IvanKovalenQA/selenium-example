import time
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

base_url = 'https://admin.shopify.com/store/ivan-dev-store-2/'
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
#Login To Shopify
browser.get(base_url)
browser.maximize_window()
browser.find_element(By.ID, 'account_email').send_keys("ivan@egnition.io")
wait = WebDriverWait(browser, 30)
button = wait.until(EC.element_to_be_clickable((By.NAME, 'commit')))
button.click()
time.sleep(6)
button_next = wait.until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
button_next.click()
password_field = wait.until(EC.element_to_be_clickable((By.NAME, 'Passwd')))
password_field.send_keys('Olga2020!')
browser.find_element(By.ID, 'passwordNext').click()
time.sleep(5)
#Get Selenium in search collections
browser.get("https://admin.shopify.com/store/ivan-dev-store-2/collections?selectedView=all&query=selenium")
time.sleep(3)
#Click on 1st element in table
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)
@pytest.fixture
def browser_fixture():
    yield browser


def test_verify_collection_title(browser_fixture):
    browser = browser_fixture
    title = browser.find_element(By.NAME, 'title')
    actual_value = title.get_attribute("value")
    expected_value = "Test Selenium Collection"
    assert actual_value == expected_value, f"Collection's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    print("Collection's title matches after creating.")
    time.sleep(1)


def test_verify_collection_description(browser_fixture):
    browser = browser_fixture
    browser.switch_to.frame('collection-description_ifr')
    description = browser.find_element(By.ID, "tinymce")
    actual_text = description.text
    expected_text = 'SELENIUMTEST'
    assert actual_text == expected_text, f"Collection's description doesn't match after creating. Expected: {expected_value}, Actual: {actual_value}"
    print("Collection's description matches after creation.")
    time.sleep(1)
    browser.switch_to.default_content()


def test_verify_collection_image(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, "//img[@class='mXwfQ']")
    src_attribute_value = element.get_attribute("src")
    search_word = 'renis'
    if "renis" in src_attribute_value:
        print(Fore.GREEN + f'Image was added successfully after creating "{search_word}".')
    else:
        print(Fore.RED + f'Image was not added successfully "{search_word}".')
    print(Style.RESET_ALL)

