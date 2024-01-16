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

#Go to MSSP2 iFrame
iframe = browser.find_element(By.NAME, 'app-iframe')
browser.switch_to.frame(iframe)
browser.execute_script("window.scrollBy(0, 300);")

#Connect locations (1st Location)
browser.find_element(By.ID, 'js-connectLocations').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[1]/div[2]/div/div').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[1]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[3]/div[2]/div/div').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[3]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(2)
#Save connection
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[5]/div/button[2]').click()
time.sleep(8)
#Connect locations (2nd Location)
browser.find_element(By.ID, 'js-connectLocations').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[1]/div[2]/div/div').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[1]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[3]/div[2]/div/div').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[3]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(2)
#Save connection
browser.find_element(By.XPATH, '//*[@id="js-connectLocationsSegment"]/div/div[5]/div/button[2]').click()
time.sleep(2)

#Default content
browser.switch_to.default_content()

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

#Go to Inventory Sync
browser.find_element(By.XPATH, '//*[@id="js-settingsMenu"]/a[3]').click()
time.sleep(2)

#Enable Inventory Sync
browser.find_element(By.ID, 'js-inventoryAutoPush').click()
time.sleep(1)

#Discrepancy mode
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[4]/div/div[5]/div/div[2]/div/div').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[4]/div/div[5]/div/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Main Shop
browser.find_element(By.XPATH, '//*[@id="js-inventoryMainStore"]/div').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="js-inventoryMainStore"]/div/div[2]/div[1]').click()
time.sleep(1)

#Button Save Settings
browser.find_element(By.XPATH, '//*[@id="js-settingsMenu"]/div/div').click()
time.sleep(2)

#Quit iFrame
browser.switch_to.default_content()

# II Go to main store and change inventory of  selenium product
browser.get('https://admin.shopify.com/store/ivan-dev-store-1/products?selectedView=all&query=Selenium')
time.sleep(3)
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
browser.execute_script("window.scrollBy(0, 300);")
time.sleep(3)
#Change inventory in Shop Location by '5'
shop_loc = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button').click()
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '.V5v1E [maxlength]').send_keys(5)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '[data-polaris-overlay] [aria-disabled]').click()
time.sleep(1)
#Change inventory in Germany Warehouse by '5'
browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button/div').click()
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '.V5v1E [maxlength]').send_keys(5)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '[data-polaris-overlay] [aria-disabled]').click()
time.sleep(20)

#II Navigate to connected story and verify that inventory was sync by the app
#Open "selenium" product in connected store
browser.get('https://admin.shopify.com/store/ivan-dev-store-2/products?selectedView=all&query=Selenium')
time.sleep(3)
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)
browser.execute_script("window.scrollBy(0, 600);")
#Navigate to inventory and verify it's quantity in Shop Location
element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button/div/div[1]/p')
actual_value = element.text
expected_value = '5'
assert actual_value == expected_value, f"Quantiy in Shop location was not sync. Expected: {expected_value}, Actual: {actual_value}"
print("Quantity in Shop location was sync successfully.")
#Verify quantity in Germany Warehouse Location
element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button/div/div[1]/p')
actual_value = element.text
expected_value = '5'
assert actual_value == expected_value, f"Quantiy in Germany Warehouse location was not sync. Expected: {expected_value}, Actual: {actual_value}"
print("Quantity in Germany Warehouse location was sync successfully.")


time.sleep(20)