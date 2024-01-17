import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, Style
from selenium import webdriver
import pyautogui
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
pyautogui.PAUSE = 0.1

# I
# Log in to Shopify

base_url = 'https://admin.shopify.com/store/ivan-dev-store-1/apps/ossp2-staging'
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
password_field.send_keys('Egnition2020!')
browser.find_element(By.ID, 'passwordNext').click()
time.sleep(15)

#TEST COMMIT TO THIS FILE
#Click on "Actions"
browser.find_element(By.CSS_SELECTOR, '.UKfhs .Polaris-LegacyStack__Item_yiyol:nth-of-type(1) .Polaris-LegacyStack__Item_yiyol:nth-of-type(1) [type]').click()
time.sleep(3)

#Click on "Settings" in Action's dropdown
browser.find_element(By.CSS_SELECTOR, '.Polaris-BlockStack--listReset_1gz07 > .Polaris-Box_375yx:nth-of-type(1) .Polaris-ActionList__Text_yj3uv').click()
time.sleep(3)

#Enter OOSP2 staging frame
iframe = browser.find_element(By.NAME, 'app-iframe')
browser.switch_to.frame(iframe)
time.sleep(1)

#Slide down
browser.execute_script("window.scrollBy(0, 300);")

#Enable Push-down OOS checkbox
browser.find_element(By.CSS_SELECTOR, '.tab-content > div:nth-of-type(1) div:nth-of-type(4) .text-center div').click()

#Enable Push-up new checkbox
browser.find_element(By.CSS_SELECTOR, '.tab-content > div:nth-of-type(1) div:nth-of-type(5) .text-center div').click()
time.sleep(7)

#WANT TO TEST BRANCHES
#UPDATEUPDATE !!
#TEST2
#Test3

