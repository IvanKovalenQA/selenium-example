import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, Style
from selenium import webdriver
import pyautogui
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# I
# Log in to Shopify

base_url = 'https://admin.shopify.com/store/ivan-dev-store-1/apps/multi-store-inventory-sync'
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get(base_url)
browser.maximize_window()

#Enter Google Account
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
time.sleep(15)

# II Go to "selenium" product in main store and change inventory level and update information
browser.get('https://admin.shopify.com/store/ivan-dev-store-1/products?selectedView=all&query=Selenium')
time.sleep(3)
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(10)
#2)Update product's information. TITLE
title = browser.find_element(By.NAME, "title").click()
time.sleep(1)
browser.find_element(By.NAME, "title").send_keys(Keys.BACK_SPACE * 21)
time.sleep(2)
browser.find_element(By.NAME, "title").send_keys('UPDATED_SELENIUM_TEST_TITLE')
#DESCRIPTION
time.sleep(1)
browser.switch_to.frame('product-description_ifr')
descr = browser.find_element(By.ID, "tinymce")
descr.clear()
descr.send_keys('UPDATED_DESCR')
browser.switch_to.default_content()
time.sleep(1)
#IMAGE
browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[2]/button/div[3]/label/span[1]/span/span[1]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[2]/div/div/div[1]/div[2]/button/span/span').click()
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, "[aria-label='Delete']").click()
time.sleep(3)
browser.find_element(By.XPATH, "//button[text()='Add from URL']").click()
time.sleep(2)
text_field = browser.find_element(By.CSS_SELECTOR, 'section .Polaris-TextField__Input_30ock')
text_field.click()
text_field.send_keys('https://cdn.shopify.com/static/sample-images/teapot.jpg')
browser.find_element(By.CSS_SELECTOR, '.Polaris-Modal-Dialog__Modal_2v9yc [aria-disabled] .Polaris-Button__Text_yj3uv').click()
time.sleep(5)
browser.execute_script("window.scrollBy(0, 500);")
#COST
cost = browser.find_element(By.NAME, 'unitCost')
cost.click()
cost.send_keys(Keys.BACK_SPACE * 7)
cost.send_keys('111')
time.sleep(2)
#Compare_At_Price
compare = browser.find_element(By.NAME, 'compareAtPrice')
compare.click()
compare.send_keys(Keys.BACK_SPACE * 7)
compare.send_keys('222')
time.sleep(1)
#Price
browser.execute_script("window.scrollBy(0, 350);")
price = browser.find_element(By.NAME, 'price')
price.click()
price.send_keys(Keys.BACK_SPACE * 7)
price.send_keys('333')
browser.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
#Update product inventory
#Change inventory in Shop Location to '10'
shop_loc = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button').click()
time.sleep(1)
shop_loc = browser.find_element(By.CSS_SELECTOR, '.V5v1E [maxlength]')
shop_loc.clear()
shop_loc.send_keys(10)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '[data-polaris-overlay] [aria-disabled]').click()
time.sleep(1)
#Change inventory in Germany Warehouse loaction to '10'
browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button/div').click()
time.sleep(1)
ger_loc = browser.find_element(By.CSS_SELECTOR, '.V5v1E [maxlength]')
ger_loc.clear()
ger_loc.send_keys(10)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '[data-polaris-overlay] [aria-disabled]').click()
time.sleep(4)
#Save
save = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Save']")))
save.click()
time.sleep(35)

#III Go to connected store and verify thah quantity was updated and all changes are observed
browser.get("https://admin.shopify.com/store/ivan-dev-store-2/products?selectedView=all&query=Selenium")
time.sleep(3)
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)

@pytest.fixture
def browser_fixture():
    yield browser


def test_verify_product_title_upd(browser_fixture):
    browser = browser_fixture
    browser.get("https://admin.shopify.com/store/ivan-dev-store-2/products?selectedView=all&query=Selenium")
    time.sleep(3)
    browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
    time.sleep(4)
    title = browser.find_element(By.NAME, 'title')
    actual_value = title.get_attribute("value")
    expected_value = "UPDATED_SELENIUM_TEST_TITLE"
    assert actual_value == expected_value, f"Product's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_description_upd(browser_fixture):
    browser = browser_fixture
    browser.switch_to.frame('product-description_ifr')
    description = browser.find_element(By.ID, "tinymce")
    actual_text = description.text
    expected_text = 'UPDATED_DESCR'
    assert actual_text == expected_text, f"Product's description doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    browser.switch_to.default_content()
    time.sleep(1)

def test_verify_product_image_upd(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.CLASS_NAME, 'ZTs54')
    src_value = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
    search_word = 'teapot'
    if search_word in src_value:
        print(Fore.GREEN + f'Image was added successfully "{search_word}".')
    else:
        print(Fore.RED + f'Image was not added successfully "{search_word}".')
    print(Style.RESET_ALL)
    time.sleep(1)

def test_verify_product_cost_upd(browser_fixture):
    browser = browser_fixture
    cost = browser.find_element(By.NAME, 'unitCost')
    actual_value = cost.get_attribute("value")
    expected_value = "111.00"
    assert actual_value == expected_value, f"Product's cost doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_compare_at_price_upd(browser_fixture):
    browser = browser_fixture
    compare = browser.find_element(By.NAME, 'compareAtPrice')
    actual_value = compare.get_attribute("value")
    expected_value = "222.00"
    assert actual_value == expected_value, f"Product's compare-at price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_price_upd(browser_fixture):
    browser = browser_fixture
    price = browser.find_element(By.NAME, 'price')
    actual_value = price.get_attribute("value")
    expected_value = "333.00"
    assert actual_value == expected_value, f"Product's price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_sku_upd(browser_fixture):
    browser = browser_fixture
    SKU = browser.find_element(By.NAME, 'sku')
    actual_value = SKU.get_attribute("value")
    expected_value = "SELENIUMSKU"
    assert actual_value == expected_value, f"Product's SKU doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_tag_upd(browser_fixture):
    browser = browser_fixture
    expected_title = "SELENIUMTAG"
    xpath_expression = f'//span[@title="{expected_title}"]'
    try:
        tag_element = browser.find_element(By.XPATH, xpath_expression)
        print(f"{expected_title} exists")
    except NoSuchElementException:
        print(f"{expected_title} doesn't exist")
    time.sleep(1)

def test_verify_quantity_in_shop_location_upd(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button/div/div[1]/p')
    actual_value = element.text
    expected_value = '10'
    assert actual_value == expected_value, f"Quantity in Shop location was not sync. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_quantity_in_germany_warehouse_location_upd(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button/div/div[1]/p')
    actual_value = element.text
    expected_value = '10'
    assert actual_value == expected_value, f"Quantity in Germany Warehouse location was not sync. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

