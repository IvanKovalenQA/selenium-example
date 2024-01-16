import time
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://admin.shopify.com/store/ivan-dev-store-1/apps/multi-store-inventory-sync'
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
#Login To Shopify
browser.get(base_url)
browser.maximize_window()
browser.find_element(By.ID, 'account_email').send_keys("ivan@egnition.io")
wait = WebDriverWait(browser, 20)
button = wait.until(EC.element_to_be_clickable((By.NAME, 'commit')))
button.click()
time.sleep(5)
browser.find_element(By.ID, 'identifierNext').click()
time.sleep(3)
browser.find_element(By.NAME, 'Passwd').send_keys('Olga2020!')
time.sleep(2)
browser.find_element(By.ID, 'passwordNext').click()
time.sleep(15)

##Go to Actions
actions = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/embedded-app/div/div[2]/div/div[3]/div/div/div[2]/div/div/div/div/div[1]/div/button')
actions.click()

#Go to Sync Settings
time.sleep(2)
browser.find_element(By.XPATH, "//button[@class='Polaris-ActionList__Item_yiyol Polaris-ActionList--default_y9uu3']//span[text()='Sync Settings']").click()

#Go to MSSP2 iFrame
iframe = browser.find_element(By.NAME, 'app-iframe')
browser.switch_to.frame(iframe)
time.sleep(2)

#Go to "Product Sync"
browser.find_element(By.XPATH, '//*[@id="js-settingsMenu"]/a[4]').click()
time.sleep(2)
browser.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

#Field "Title"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[1]/div[2]/div/div').click()
time.sleep(1)
#Title "Upon Creation"
browser.find_element(By.CSS_SELECTOR, ".js-product-fields .field-class-title [data-value='create_only']").click()
time.sleep(1)
#Field Description
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[2]/div[2]/div/div').click()
time.sleep(1)
#Description "Upon Creation"
browser.find_element(By.CSS_SELECTOR, ".js-product-fields .field-class-bodyHtml [data-value='create_only']").click()
time.sleep(1)
##Field PageTitle(SEO)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[3]/div[2]/div/div').click()
time.sleep(1)
#PageTitle(SEO) "Upon Creation "
browser.find_element(By.CSS_SELECTOR, ".js-product-fields .field-class-seoTitle [data-value='create_only']").click()
time.sleep(1)
#Field Description(SEO)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[4]/div[2]/div/div').click()
time.sleep(1)
#Description (SEO) "Upon Creation"
browser.find_element(By.CSS_SELECTOR, ".js-product-fields .field-class-seoBodyHtml [data-value='create_only']").click()
time.sleep(1)
#Field URL and handle
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[6]/div[2]/div/div').click()
time.sleep(1)
#URL and handle "Upon Creation"
browser.find_element(By.CSS_SELECTOR, ".field-class-handle [data-value='create_only']").click()
time.sleep(1)
#Field Product Type
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[7]/div[2]/div/div').click()
time.sleep(1)
#Product Type "Upon Creation"
browser.find_element(By.CSS_SELECTOR, ".field-class-type [data-value='create_only']").click()
time.sleep(1)
#Field Product Images/Media
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[9]/div[2]/div/div').click()
time.sleep(1)
#Images/Media "Upon creation"
browser.find_element(By.CSS_SELECTOR, ".js-product-fields .field-class-images [data-value='create_only']").click()
time.sleep(1)
#Field Product tags
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[11]/div[2]/div/div').click()
time.sleep(1)
#Product Tags "Upon Creation"
browser.find_element(By.CSS_SELECTOR, ".field-class-tags [data-value='create_only']").click()
time.sleep(1)
#Field Price
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[14]/div[2]/div/div').click()
time.sleep(1)
#Price "Upon Creation"
browser.find_element(By.CSS_SELECTOR, ".field-class-price [data-value='create_only']").click()
time.sleep(1)

#Button Save Settings
browser.find_element(By.XPATH, '//*[@id="js-settingsMenu"]/div/div').click()
time.sleep(7)
#Quit iFrame
browser.switch_to.default_content()

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
time.sleep(35)

#II
#Verify that product from main store was added to connected store

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