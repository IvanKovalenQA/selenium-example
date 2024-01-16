import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import logging
from colorama import Fore, Style
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
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
    time.sleep(1)


def test_verify_collection_image(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, "//img[@class='mXwfQ']")
    src_attribute_value = element.get_attribute("src")
    search_word = 'renis'
    if "renis" in src_attribute_value:
        print(Fore.GREEN + f'Image was added successfully "{search_word}".')
    else:
        print(Fore.RED + f'Image was not added successfully "{search_word}".')
    print(Style.RESET_ALL)
    time.sleep(1)



def test_verify_product_title(browser_fixture):
    browser = browser_fixture
    browser.get("https://admin.shopify.com/store/ivan-dev-store-2/products?selectedView=all&query=Selenium")
    time.sleep(3)
    browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
    time.sleep(4)
    title = browser.find_element(By.NAME, 'title')
    actual_value = title.get_attribute("value")
    expected_value = "Test Selenium Product"
    assert actual_value == expected_value, f"Product's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

browser.execute_script("window.scrollBy(0, 450);")

def test_verify_product_description(browser_fixture):
    browser = browser_fixture
    browser.switch_to.frame('product-description_ifr')
    description = browser.find_element(By.ID, "tinymce")
    actual_text = description.text
    expected_text = 'SELENIUMTEST'
    assert actual_text == expected_text, f"Product's description doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    browser.switch_to.default_content()
    browser.execute_script("window.scrollBy(0, 450);")
    time.sleep(1)

def test_verify_product_image(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.CLASS_NAME, 'ZTs54')
    src_value = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
    search_word = 'shoes'
    if search_word in src_value:
        print(Fore.GREEN + f'Image was added successfully "{search_word}".')
    else:
        print(Fore.RED + f'Image was not added successfully "{search_word}".')
    print(Style.RESET_ALL)
    time.sleep(1)

def test_verify_product_cost(browser_fixture):
    browser = browser_fixture
    browser.execute_script("window.scrollBy(0, 500);")
    cost = browser.find_element(By.NAME, 'unitCost')
    actual_value = cost.get_attribute("value")
    expected_value = "100.00"
    assert actual_value == expected_value, f"Product's cost doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_compare_at_price(browser_fixture):
    browser = browser_fixture
    compare = browser.find_element(By.NAME, 'compareAtPrice')
    actual_value = compare.get_attribute("value")
    expected_value = "50.00"
    assert actual_value == expected_value, f"Product's compare-at price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_price(browser_fixture):
    browser = browser_fixture
    price = browser.find_element(By.NAME, 'price')
    actual_value = price.get_attribute("value")
    expected_value = "10.00"
    assert actual_value == expected_value, f"Product's price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_sku(browser_fixture):
    browser = browser_fixture
    SKU = browser.find_element(By.NAME, 'sku')
    actual_value = SKU.get_attribute("value")
    expected_value = "SELENIUMSKU"
    assert actual_value == expected_value, f"Product's SKU doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_tag(browser_fixture):
    browser = browser_fixture
    expected_title = "SELENIUMTAG"
    xpath_expression = f'//span[@title="{expected_title}"]'
    try:
        tag_element = browser.find_element(By.XPATH, xpath_expression)
        print(f"{expected_title} exists")
    except NoSuchElementException:
        print(f"{expected_title} doesn't exist")
    time.sleep(1)

def test_verify_quantity_in_shop_location(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button/div/div[1]/p')
    actual_value = element.text
    expected_value = '5'
    assert actual_value == expected_value, f"Quantity in Shop location was not sync. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_quantity_in_germany_warehouse_location(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button/div/div[1]/p')
    actual_value = element.text
    expected_value = '5'
    assert actual_value == expected_value, f"Quantity in Germany Warehouse location was not sync. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)




