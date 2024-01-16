import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, Style
from selenium import webdriver
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

#II
#Change MSSP2's settings
#Go to Actions
actions = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="AppFrameMain"]/div/div/embedded-app/div/div[2]/div/div[3]/div/div/div[2]/div/div/div/div/div[1]/div/button')))
actions.click()
#Go to Sync Settings
time.sleep(2)
browser.find_element(By.XPATH, "//button[@class='Polaris-ActionList__Item_yiyol Polaris-ActionList--default_y9uu3']//span[text()='Sync Settings']").click()
#Go to MSSP2 iFrame
iframe = browser.find_element(By.NAME, 'app-iframe')
browser.switch_to.frame(iframe)
time.sleep(2)
#Go to Collection Sync
browser.find_element(By.XPATH, '//*[@id="js-settingsMenu"]/a[5]').click()
time.sleep(5)
#Enable Collection Sync checkbox
browser.find_element(By.ID, 'js-collectionAutoUpdate').click()
time.sleep(1)
#Enable Collection Creation checkbox
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div').click()
time.sleep(1)
browser.execute_script("window.scrollBy(0, 300);")
#Field Title
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[1]/div[2]/div/div').click()
time.sleep(1)
#Title Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field Description
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[2]/div[2]/div/div').click()
time.sleep(1)
#Description Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Collection Image
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[3]/div[2]/div/div').click()
time.sleep(1)
browser.execute_script("window.scrollBy(0, 300);")
#Collection Image Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Collection Availability
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[4]/div[2]/div/div').click()
time.sleep(1)
#Collection Availability  Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[4]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Sort Order
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[5]/div[2]/div/div').click()
time.sleep(1)
#Sort Order Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[5]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Page Title (SEO)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[6]/div[2]/div/div').click()
time.sleep(1)
browser.execute_script("window.scrollBy(0, 300);")
#Page Title (SEO) Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[6]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Description (SEO)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[7]/div[2]/div/div').click()
time.sleep(1)
#Description (SEO) Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[7]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Metafields
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[8]/div[2]/div/div').click()
time.sleep(1)
#Metafields Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[8]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Conditions and Rules
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[9]/div[2]/div/div').click()
time.sleep(1)
#Conditions and Rules Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[9]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field Push Products
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[10]/div[2]/div/div').click()
time.sleep(1)
#Push Products Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[10]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Order of Products
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[11]/div[2]/div/div').click()
time.sleep(1)
#Order of Products Every Update
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[6]/div[2]/div[2]/div/div[11]/div[2]/div/div/div[2]/div[1]').click()
#Click Save
browser.find_element(By.XPATH, '//*[@id="js-settingsMenu"]/div/div').click()

time.sleep(10)