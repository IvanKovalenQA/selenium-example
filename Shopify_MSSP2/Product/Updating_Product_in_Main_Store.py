import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://admin.shopify.com/store/ivan-dev-store-1/apps/multi-store-inventory-sync'
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get(base_url)
browser.maximize_window()
#I Enter Google Account
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

#II
# 1)Go to existing product "selenium" in main store
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
#IMAGE *it's need to verify what shall do with image...*
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
price = browser.find_element(By.NAME, 'price')
price.click()
price.send_keys(Keys.BACK_SPACE * 7)
price.send_keys('333')
time.sleep(1)

#Change inventory level in Shop location
#Change inventory in Shop Location by '10'
shop_loc = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button').click()
time.sleep(1)
shop_loc = browser.find_element(By.CSS_SELECTOR, '.V5v1E [maxlength]')
shop_loc.clear()
shop_loc.send_keys(10)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '[data-polaris-overlay] [aria-disabled]').click()
time.sleep(1)
#Change inventory in Germany Warehouse loaction by '1'
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

time.sleep(10)




