import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from colorama import Fore, Style
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://admin.shopify.com/store/ivan-dev-store-2/products?selectedView=all'
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
#Get Selenium in search products
browser.get("https://admin.shopify.com/store/ivan-dev-store-2/products?selectedView=all&query=Selenium")
time.sleep(3)
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)
#Verify that title in connected store matches title in main store
title = browser.find_element(By.NAME, 'title')
actual_value = title.get_attribute("value")
expected_value = "Test Selenium Product"
assert actual_value == expected_value, f"Product's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's title matches.")
time.sleep(1)
#Verify that description in connected store matches description in main store
browser.switch_to.frame('product-description_ifr')
description = browser.find_element(By.ID, "tinymce")
actual_text = description.text
expected_text = 'SELENIUMTEST'
assert actual_text == expected_text, f"Product's description doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's description matches.")
time.sleep(1)
browser.switch_to.default_content()
#Verify that product's image exists
element = browser.find_element(By.CLASS_NAME, 'ZTs54')
src_value = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
search_word = 'shoes'
if search_word in src_value:
    print(Fore.GREEN + f'Image was added succesfully "{search_word}".')
else:
    print(Fore.RED + f'Image was not added succesfully "{search_word}".')

print(Style.RESET_ALL)

browser.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
#Verify that product's cost in connected store matches cost in main store
cost = browser.find_element(By.NAME, 'unitCost')
actual_value = cost.get_attribute("value")
expected_value = "100.00"
assert actual_value == expected_value, f"Product's cost doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's cost matches.")
time.sleep(1)
#Verify that product's compare-at price in connected store matches compare-at price in main store
compare = browser.find_element(By.NAME, 'compareAtPrice')
actual_value = compare.get_attribute("value")
expected_value = "50.00"
assert actual_value == expected_value, f"Product's compare-at price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's compare-at price matches.")
time.sleep(1)
#Verify that product's price in connected store matches price in main store
price = browser.find_element(By.NAME, 'price')
actual_value = price.get_attribute("value")
expected_value = "10.00"
assert actual_value == expected_value, f"Product's price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's price matches.")
time.sleep(1)
#Verify that product's SKU in connected store matches SKU in main store
SKU = browser.find_element(By.NAME, 'sku')
actual_value = SKU.get_attribute("value")
expected_value = "SELENIUMSKU"
assert actual_value == expected_value, f"Product's SKU doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's SKU matches.")
time.sleep(1)
#Verify that product's tag in connected store matches description in main store
expected_title = "SELENIUMTAG"
xpath_expression = f'//span[@title="{expected_title}"]'
try:
    tag_element = browser.find_element(By.XPATH, xpath_expression)
    print(f"{expected_title} exists")
except NoSuchElementException:
    print(f"{expected_title} doesn't exists")

#Verify quantity in Shop Location
element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button/div/div[1]/p')
actual_value = element.text
expected_value = '5'
assert actual_value == expected_value, f"Quantiy in Shop location was not sync. Expected: {expected_value}, Actual: {actual_value}"
print("Quantity in Shop location was sync successfully after creating.")

#Verify quantity in Germany warehouse loaction

element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button/div/div[1]/p')
actual_value = element.text
expected_value = '5'
assert actual_value == expected_value, f"Quantiy in Germany Warehouse location was not sync. Expected: {expected_value}, Actual: {actual_value}"
print("Quantity in Germany Warehouse location was sync successfully after creating.")




time.sleep(20)