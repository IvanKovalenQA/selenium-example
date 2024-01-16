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
pyautogui.PAUSE = 0.1
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

#Create New Product in Shopify Admin

#Go To Shopify Admin to
browser.get('https://admin.shopify.com/store/ivan-dev-store-1/products?selectedView=all')
time.sleep(2)
#Add product in main store
add_product = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add product']")))
add_product.click()
#Add title to product
title = wait.until(EC.element_to_be_clickable((By.NAME, "title")))
title.send_keys('Test Selenium Product')
time.sleep(3)
#Add description to product
browser.switch_to.frame('product-description_ifr')
browser.find_element(By.ID, "tinymce").send_keys("SELENIUMTEST")
time.sleep(3)
#Add image via "ADD FROM URL"
browser.switch_to.default_content()
browser.find_element(By.XPATH, "//button[text()='Add from URL']").click()
time.sleep(2)
text_field = browser.find_element(By.CSS_SELECTOR, 'section .Polaris-TextField__Input_30ock')
text_field.click()
text_field.send_keys('https://cdn.shopify.com/static/sample-images/shoes.jpeg')
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="PolarisPortalsContainer"]/div[11]/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/button[2]/span/span').click()
time.sleep(3)
#Add "Cost per Item" to product
browser.find_element(By.NAME, 'unitCost').send_keys("100")
time.sleep(3)
#Add comare-at price to product
browser.find_element(By.NAME, 'compareAtPrice').send_keys('50')
time.sleep(3)
#Add Price to product
browser.find_element(By.NAME, 'price').send_keys('10')
time.sleep(3)
#Add SKU to product
browser.find_element(By.NAME, 'sku').send_keys('SELENIUMSKU')
time.sleep(3)
#Add tags to product
tags = browser.find_element(By.NAME, 'tags')
tags.send_keys('SELENIUMTAG')
time.sleep(1)
tags.send_keys(Keys.ENTER)
time.sleep(3)
#Add inventory in Shop Location by '5'
browser.execute_script("window.scrollBy(0, 300);")
shop_loc = browser.find_element(By.NAME, 'inventoryLevels[1]')
shop_loc.send_keys(5)
time.sleep(2)
#Add inventory in Germany Warehouse by '5'
germ_loc = browser.find_element(By.NAME, 'inventoryLevels[0]')
germ_loc.send_keys(5)
time.sleep(2)
#Save product
save = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Save']")))
save.click()
time.sleep(10)

#Create Manual Collection In Main Store
#Go to Shopify Collections
browser.get('https://admin.shopify.com/store/ivan-dev-store-1/collections?selectedView=all')
time.sleep(2)
#Add New Manual Collection
browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[1]/div/div/div[2]/div[2]/div').click()
time.sleep(5)
#Add Title
browser.find_element(By.NAME, 'title').send_keys('Test Selenium Collection')
time.sleep(1)
#Add description
browser.switch_to.frame('collection-description_ifr')
browser.find_element(By.ID, "tinymce").send_keys("SELENIUMTEST")
time.sleep(2)
browser.switch_to.default_content()
#Add image
browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div').click()
time.sleep(1)
file_path = '//Users/user/Downloads/renis.jpeg'
pyautogui.write(file_path)
time.sleep(5)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
#Click "Save" button
browser.find_element(By.XPATH, '//*[@id="AppFrame"]/div/div[4]/div/div[2]/div[2]/div/div[2]/button').click()
time.sleep(10)
#II Adding product to existing Manual Collection
#search = browser.find_element(By.CSS_SELECTOR, '.Polaris-LegacyStack--distributionFill_1c1lq .Polaris-TextField__Input_30ock')
#search.click()
#time.sleep(1)
#search.send_keys("SSelenium")
#time.sleep(5)
#Add "selenium" product
#browser.find_element(By.XPATH, '//*[@id="PolarisPortalsContainer"]/div[48]/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/div').click()
#browser.find_element(By.XPATH, '//*[@id="PolarisPortalsContainer"]/div[48]/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/button[2]').click()
#time.sleep(7)

#IV
#Verify that product from main store was added to connected store

#Go to connected store and search "selenium" in products
browser.get('https://admin.shopify.com/store/ivan-dev-store-2/products?selectedView=all&query=Selenium')
time.sleep(3)
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)

@pytest.fixture
def browser_fixture():
    yield browser

def test_verify_product_title_creat(browser_fixture):
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

def test_verify_product_description_creat(browser_fixture):
    browser = browser_fixture
    browser.switch_to.frame('product-description_ifr')
    description = browser.find_element(By.ID, "tinymce")
    actual_text = description.text
    expected_text = 'SELENIUMTEST'
    assert actual_text == expected_text, f"Product's description doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    browser.switch_to.default_content()
    browser.execute_script("window.scrollBy(0, 450);")
    time.sleep(1)

def test_verify_product_image_creat(browser_fixture):
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

def test_verify_product_cost_creat(browser_fixture):
    browser = browser_fixture
    browser.execute_script("window.scrollBy(0, 500);")
    cost = browser.find_element(By.NAME, 'unitCost')
    actual_value = cost.get_attribute("value")
    expected_value = "100.00"
    assert actual_value == expected_value, f"Product's cost doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_compare_at_price_creat(browser_fixture):
    browser = browser_fixture
    compare = browser.find_element(By.NAME, 'compareAtPrice')
    actual_value = compare.get_attribute("value")
    expected_value = "50.00"
    assert actual_value == expected_value, f"Product's compare-at price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_price_creat(browser_fixture):
    browser = browser_fixture
    price = browser.find_element(By.NAME, 'price')
    actual_value = price.get_attribute("value")
    expected_value = "10.00"
    assert actual_value == expected_value, f"Product's price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_sku_creat(browser_fixture):
    browser = browser_fixture
    SKU = browser.find_element(By.NAME, 'sku')
    actual_value = SKU.get_attribute("value")
    expected_value = "SELENIUMSKU"
    assert actual_value == expected_value, f"Product's SKU doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_product_tag_creat(browser_fixture):
    browser = browser_fixture
    expected_title = "SELENIUMTAG"
    xpath_expression = f'//span[@title="{expected_title}"]'
    try:
        tag_element = browser.find_element(By.XPATH, xpath_expression)
        print(f"{expected_title} exists")
    except NoSuchElementException:
        print(f"{expected_title} doesn't exist")
    time.sleep(1)

def test_verify_quantity_in_shop_location_creat(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button/div/div[1]/p')
    actual_value = element.text
    expected_value = '5'
    assert actual_value == expected_value, f"Quantity in Shop location was not sync. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

def test_verify_quantity_in_germany_warehouse_location_creat(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button/div/div[1]/p')
    actual_value = element.text
    expected_value = '5'
    assert actual_value == expected_value, f"Quantity in Germany Warehouse location was not sync. Expected: {expected_value}, Actual: {actual_value}"
    time.sleep(1)

# VERIFY THAT MANUAL COLLECTION EXISTS IN CONNECTED STORE
#Get Selenium in search collections
browser.get("https://admin.shopify.com/store/ivan-dev-store-2/collections?selectedView=all&query=selenium")
time.sleep(3)
#Click on 1st element in table
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)

def test_verify_collection_title_creat(browser_fixture):
    browser = browser_fixture
    title = browser.find_element(By.NAME, 'title')
    actual_value = title.get_attribute("value")
    expected_value = "Test Selenium Collection"
    assert actual_value == expected_value, f"Collection's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    print("Collection's title matches after creating.")
    time.sleep(1)


def test_verify_collection_description_creat(browser_fixture):
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


def test_verify_collection_image_creat(browser_fixture):
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

# III Go to "selenium" product in main store and change inventory level and update information
browser.get('https://admin.shopify.com/store/ivan-dev-store-1/products?selectedView=all&query=Selenium')
time.sleep(3)
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(5)
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
browser.find_element(By.XPATH, '//*[@id="PolarisPortalsContainer"]/div[11]/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/button[2]/span/span').click()
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
browser.execute_script("window.scrollBy(0, 300);")
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
browser.execute_script("window.scrollBy(0, 300);")

time.sleep(10)

#CHANGE "SELENIUM" MANUAL COLLECTION IN MAIN STORE
# 1)Go to existing collection "selenium" in main store
#Get Selenium in search collections
browser.get("https://admin.shopify.com/store/ivan-dev-store-1/collections?selectedView=all&query=selenium")
time.sleep(3)
#Click on 1st element in table
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)
#2)Update collection's information. TITLE
title = browser.find_element(By.NAME, "title").click()
time.sleep(1)
browser.find_element(By.NAME, "title").send_keys(Keys.BACK_SPACE * 24)
time.sleep(2)
browser.find_element(By.NAME, "title").send_keys('UPDATED_SELENIUM_COLLECTION_TEST_TITLE')
time.sleep(2)
#DESCRIPTION
browser.switch_to.frame('collection-description_ifr')
description = browser.find_element(By.ID, "tinymce")
description.clear()
description.send_keys("SELENIUMTEST_UPDATED")
time.sleep(2)
browser.switch_to.default_content()
#Change image
browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[2]/div[2]/header/div/div[2]/div/button/span/span').click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, '.Polaris-ActionList--destructive_zy6o5 .Polaris-ActionList__Text_yj3uv').click()
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div').click()
time.sleep(2)
file_path = '//Users/user/Downloads/tshirt.jpg'
time.sleep(2)
pyautogui.write(file_path)
time.sleep(5)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')
time.sleep(5)
#Click "Save" button
browser.find_element(By.XPATH, '//*[@id="AppFrame"]/div/div[4]/div/div[2]/div[2]/div/div[2]/button').click()
time.sleep(5)


#IV Go to 'selenium' product in connected store and verify that all changes was made by the app
browser.get("https://admin.shopify.com/store/ivan-dev-store-2/products?selectedView=all&query=Selenium")
time.sleep(3)
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)
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

#VERIFY THAT "SELENIUM" MANUAL COLLECTION SUCCESSFULLY UPDATED IN CONNECTED STORE
#Get Selenium in search collections
browser.get("https://admin.shopify.com/store/ivan-dev-store-2/collections?selectedView=all&query=selenium")
time.sleep(3)
#Click on 1st element in table
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)

def test_verify_collection_title_upd(browser_fixture):
    browser = browser_fixture
    title = browser.find_element(By.NAME, 'title')
    actual_value = title.get_attribute("value")
    expected_value = "UPDATED_SELENIUM_COLLECTION_TEST_TITLE"
    assert actual_value == expected_value, f"Collection's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
    print("Collection's title matches after updating.")
    time.sleep(1)


def test_verify_collection_description_upd(browser_fixture):
    browser = browser_fixture
    browser.switch_to.frame('collection-description_ifr')
    description = browser.find_element(By.ID, "tinymce")
    actual_text = description.text
    expected_text = 'SELENIUMTEST_UPDATED'
    assert actual_text == expected_text, f"Collection's description doesn't match after updating. Expected: {expected_value}, Actual: {actual_value}"
    print("Collection's description matches after updating.")
    time.sleep(1)
    browser.switch_to.default_content()


def test_verify_collection_image_upd(browser_fixture):
    browser = browser_fixture
    element = browser.find_element(By.XPATH, "//img[@class='mXwfQ']")
    src_attribute_value = element.get_attribute("src")
    search_word = 'tshirt'
    if "tshirt" in src_attribute_value:
        print(Fore.GREEN + f'Image was updated successfully "{search_word}".')
    else:
        print(Fore.RED + f'Image was not updated successfully "{search_word}".')
    print(Style.RESET_ALL)
    time.sleep(1)



time.sleep(20)