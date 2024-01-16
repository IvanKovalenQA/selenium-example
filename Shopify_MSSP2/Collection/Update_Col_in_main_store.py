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
browser.find_element(By.XPATH, '//*[@id="AppFrame"]/div/div[4]/div/div[2]/div[2]/div/div[2]/button').click()
time.sleep(30)

