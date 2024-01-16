import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://admin.shopify.com/store/ivan-dev-store-1/products?selectedView=all'
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
#Adding New Product to Shopify
add_product = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add product']")))
add_product.click()
#Title
title = wait.until(EC.element_to_be_clickable((By.NAME, "title")))
title.send_keys('Test Selenium Product')
time.sleep(3)
#Description
browser.switch_to.frame('product-description_ifr')
browser.find_element(By.ID, "tinymce").send_keys("SELENIUMTEST")
time.sleep(3)
browser.switch_to.default_content()
#Image
browser.find_element(By.XPATH, "//button[text()='Add from URL']").click()
time.sleep(2)
text_field = browser.find_element(By.CSS_SELECTOR, 'section .Polaris-TextField__Input_30ock')
text_field.click()
text_field.send_keys('https://cdn.shopify.com/static/sample-images/shoes.jpeg')
browser.find_element(By.XPATH, '//*[@id="PolarisPortalsContainer"]/div[11]/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/button[2]/span/span').click()


time.sleep(2)

browser.find_element(By.NAME, 'unitCost').send_keys("100")
time.sleep(3)
browser.find_element(By.NAME, 'compareAtPrice').send_keys('50')
time.sleep(3)
browser.find_element(By.NAME, 'price').send_keys('10')
time.sleep(3)
browser.find_element(By.NAME, 'sku').send_keys('SELENIUMSKU')
time.sleep(3)
tags = browser.find_element(By.NAME, 'tags')
tags.send_keys('SELENIUMTAG')
time.sleep(1)
tags.send_keys(Keys.ENTER)
time.sleep(3)


#Adding quantitiy in Shop location

#Add inventory in Shop Location by '5'
browser.execute_script("window.scrollBy(0, 300);")
shop_loc = browser.find_element(By.NAME, 'inventoryLevels[1]')
shop_loc.send_keys(5)
time.sleep(2)
#Add inventory in Germany Warehouse by '5'
germ_loc = browser.find_element(By.NAME, 'inventoryLevels[0]')
germ_loc.send_keys(5)
time.sleep(2)


#SAVE
save = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Save']")))
save.click()
time.sleep(20)


