import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore, Style
import pyautogui
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
#Go to Collection with word "Selenium"
browser.get('https://admin.shopify.com/store/ivan-dev-store-1/collections?selectedView=all&query=selenium')
time.sleep(5)
#Click on 1st element from table
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)
#II Adding product to existing Manual Collection
search = browser.find_element(By.CSS_SELECTOR, '.Polaris-LegacyStack--distributionFill_1c1lq .Polaris-TextField__Input_30ock')
search.click()
time.sleep(1)
search.send_keys("SSelenium")
time.sleep(5)
#Add "selenium" product
browser.find_element(By.XPATH, '//*[@id="PolarisPortalsContainer"]/div[48]/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/div').click()
browser.find_element(By.XPATH, '//*[@id="PolarisPortalsContainer"]/div[48]/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/button[2]').click()
time.sleep(10)