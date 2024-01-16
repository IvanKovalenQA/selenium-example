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

# Connect locations and enable inventory sync
#Connect locations (1st Location)
iframe = browser.find_element(By.NAME, 'app-iframe')
browser.switch_to.frame(iframe)
browser.execute_script("window.scrollBy(0, 300);")
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
browser.execute_script("window.scrollBy(0, -300);")
time.sleep(1)
##Go to Collection Sync
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
time.sleep(2)

#Go to "Product Sync"
browser.find_element(By.XPATH, '//*[@id="js-settingsMenu"]/a[4]').click()
time.sleep(2)
browser.execute_script("window.scrollTo(0, 0);")
time.sleep(1)
#Checkbox "Product Sync"
browser.find_element(By.ID, 'js-productAutoUpdate').click()
time.sleep(1)
#Checkbox Create Product
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[1]/div[3]/div/div[2]/div/div').click()
time.sleep(1)
#Field "Title"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[1]/div[2]/div/div').click()
time.sleep(1)
#Title "Every Update"
browser.find_element(By.CSS_SELECTOR, 'div.item[data-value="every_update"]').click()
time.sleep(1)
#Field Description
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[2]/div[2]/div/div').click()
time.sleep(1)
#Description "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field PageTitle(SEO)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[3]/div[2]/div/div').click()
time.sleep(1)
#PageTitle(SEO) "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Description(SEO)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[4]/div[2]/div/div').click()
time.sleep(1)
#Description (SEO) "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[4]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Metafields
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[5]/div[2]/div/div').click()
time.sleep(1)
#Metafields "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[5]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field URL and handle
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[6]/div[2]/div/div').click()
time.sleep(1)
#URL and handle "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[6]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Product Type
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[7]/div[2]/div/div').click()
time.sleep(1)
#Product Type "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[7]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Vendor
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[8]/div[2]/div/div').click()
time.sleep(1)
#Vendor "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[8]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Product Images/Media
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[9]/div[2]/div/div').click()
time.sleep(1)
#Images/Media "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[9]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Product Status
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[10]/div[2]/div/div').click()
time.sleep(1)
#Product Status "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[10]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Product tags
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[11]/div[2]/div/div').click()
time.sleep(1)
#Product Tags "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[11]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Publish
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[12]/div[2]/div/div').click()
time.sleep(1)
#Publish "Every Update"
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[12]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field Variant Title
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[13]/div[2]/div/div').click()
time.sleep(1)
#Variant Title "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[13]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field Price
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[14]/div[2]/div/div').click()
time.sleep(1)
#Price "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[14]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field Compare at Price
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[16]/div[2]/div/div').click()
time.sleep(1)
#Compare at Price "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[16]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field Cost
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[17]/div[2]/div/div').click()
time.sleep(1)
#Cost "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[17]/div[2]/div/div/div[2]/div[1]').click()
browser.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
#Field Country code of origin
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[18]/div[2]/div/div').click()
time.sleep(1)
#Country code of origin "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[18]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Province code of origin
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[19]/div[2]/div/div').click()
time.sleep(1)
#Province Code of Origin "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[19]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Harmonized system code (HSC)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[20]/div[2]/div/div').click()
time.sleep(1)
#Harmonized system code (HSC) "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[20]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Charge tax on this product
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[21]/div[2]/div/div').click()
time.sleep(1)
#Charge tax on this product "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[21]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field Barcode
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[23]/div[2]/div/div').click()
time.sleep(1)
#Barcode "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[23]/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
#Field Track quantity (Shopify)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[24]/div[2]/div/div').click()
time.sleep(1)
#Track quantity (Shopify) "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[24]/div[2]/div/div/div[2]/div[2]').click()
browser.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
#Field Continue selling when out of stock
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[25]/div[2]/div/div').click()
time.sleep(1)
#Continue selling when out of stock "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[25]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field This is a physical product (requires shipping)
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[26]/div[2]/div/div').click()
time.sleep(1)
#This is a physical product (requires shipping) "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[26]/div[2]/div/div/div[2]/div[2]').click()
time.sleep(1)
#Field Weight & unit
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[27]/div[2]/div/div').click()
time.sleep(1)
#Weight & unit "Every Update"
browser.find_element(By.XPATH, '//*[@id="js-settingsForm"]/div/div[5]/div[2]/div[2]/div/div[27]/div[2]/div/div/div[2]/div[1]').click()
browser.execute_script("window.scrollBy(0, 1500);")
time.sleep(3)
#Button Save Settings
browser.find_element(By.XPATH, '//*[@id="js-settingsMenu"]/div/div').click()
time.sleep(7)
#Quit iFrame
browser.switch_to.default_content()

#III
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
#Verify that title in connected store matches title in main store
title = browser.find_element(By.NAME, 'title')
actual_value = title.get_attribute("value")
expected_value = "Test Selenium Product"
assert actual_value == expected_value, f"Product's title doesn't match after creating. Expected: {expected_value}, Actual: {actual_value}"
print("Product's title matches after product creating.")
time.sleep(1)
#Verify that description in connected store matches description in main store
browser.switch_to.frame('product-description_ifr')
description = browser.find_element(By.ID, "tinymce")
actual_text = description.text
expected_text = 'SELENIUMTEST'
assert actual_text == expected_text, f"Product's description doesn't match after creating. Expected: {expected_value}, Actual: {actual_value}"
print("Product's description matches after creating.")
time.sleep(1)
#Verify that product's image exists
browser.switch_to.default_content()
element = browser.find_element(By.CLASS_NAME, 'ZTs54')
src_value = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
search_word = 'shoes'
if search_word in src_value:
    print(Fore.GREEN + f'Image was added succesfully after product creating. "{search_word}".')
else:
    print(Fore.RED + f'Image was not added succesfully after product creating. "{search_word}".')

print(Style.RESET_ALL)


time.sleep(1)
browser.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
#Verify that product's cost in connected store matches cost in main store
cost = browser.find_element(By.NAME, 'unitCost')
actual_value = cost.get_attribute("value")
expected_value = "100.00"
assert actual_value == expected_value, f"Product's cost doesn't match after product creating. Expected: {expected_value}, Actual: {actual_value}"
print("Product's cost matches after product creating.")
time.sleep(1)
#Verify that product's compare-at price in connected store matches compare-at price in main store
compare = browser.find_element(By.NAME, 'compareAtPrice')
actual_value = compare.get_attribute("value")
expected_value = "50.00"
assert actual_value == expected_value, f"Product's compare-at price doesn't match after product creating. Expected: {expected_value}, Actual: {actual_value}"
print("Product's compare-at price matches after product creating.")
time.sleep(1)
#Verify that product's price in connected store matches price in main store
price = browser.find_element(By.NAME, 'price')
actual_value = price.get_attribute("value")
expected_value = "10.00"
assert actual_value == expected_value, f"Product's price doesn't match after product creating. Expected: {expected_value}, Actual: {actual_value}"
print("Product's price matches after product creating.")
time.sleep(1)
#Verify that product's SKU in connected store matches SKU in main store
SKU = browser.find_element(By.NAME, 'sku')
actual_value = SKU.get_attribute("value")
expected_value = "SELENIUMSKU"
assert actual_value == expected_value, f"Product's SKU doesn't match after product creating. Expected: {expected_value}, Actual: {actual_value}"
print("Product's SKU matches after product creating.")
time.sleep(1)
#Verify that product's tag in connected store matches description in main store
expected_title = "SELENIUMTAG"
xpath_expression = f'//span[@title="{expected_title}"]'
try:
    tag_element = browser.find_element(By.XPATH, xpath_expression)
    print(f"{expected_title} exists after product creating")
except NoSuchElementException:
    print(f"{expected_title} doesn't exists after product creating")
time.sleep(2)
browser.execute_script("window.scrollBy(0, 300);")

##Verify quantity in Shop Location
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

# VERIFY THAT MANUAL COLLECTION EXISTS IN CONNECTED STORE
#Get Selenium in search collections
browser.get("https://admin.shopify.com/store/ivan-dev-store-2/collections?selectedView=all&query=selenium")
time.sleep(3)
#Click on 1st element in table
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)
#Verify collection's title in connected store
title = browser.find_element(By.NAME, 'title')
actual_value = title.get_attribute("value")
expected_value = "Test Selenium Collection"
assert actual_value == expected_value, f"Collection's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Collection's title matches after creating.")
time.sleep(1)
#Verify collection's description in connected store
browser.switch_to.frame('collection-description_ifr')
description = browser.find_element(By.ID, "tinymce")
actual_text = description.text
expected_text = 'SELENIUMTEST'
assert actual_text == expected_text, f"Collection's description doesn't match after creating. Expected: {expected_value}, Actual: {actual_value}"
print("Collection's description matches after creating.")
time.sleep(1)
browser.switch_to.default_content()
try:
    element = browser.find_element(By.XPATH, "//img[@class='mXwfQ']")
    src_attribute_value = element.get_attribute("src")
    search_word = 'renis'

    if search_word in src_attribute_value:
        print(Fore.GREEN + f'Image was added successfully "{search_word}".')
    else:
        print(Fore.RED + f'Image was not added successfully "{search_word}".')

except NoSuchElementException:
    print(Fore.RED + 'Image doesnt exist.')

finally:
    print(Style.RESET_ALL)
time.sleep(10)


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
#Verify title
title = browser.find_element(By.NAME, 'title')
actual_value = title.get_attribute("value")
expected_value = "UPDATED_SELENIUM_TEST_TITLE"
assert actual_value == expected_value, f"Product's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's title matches after updating.")
time.sleep(1)
#Verify description
browser.switch_to.frame('product-description_ifr')
description = browser.find_element(By.ID, "tinymce")
actual_text = description.text
expected_text = 'UPDATED_DESCR'
assert actual_text == expected_text, f"Product's description doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's description matches after updating.")
time.sleep(1)
browser.switch_to.default_content()
#IMAGE *....*
browser.switch_to.default_content()
element = browser.find_element(By.CLASS_NAME, 'ZTs54')
src_value = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
search_word = 'teapot'
if search_word in src_value:
    print(Fore.GREEN + f'Image was added successfully after product updating. "{search_word}".')
else:
    print(Fore.RED + f'Image was not added successfully after product updating. "{search_word}".')

print(Style.RESET_ALL)
browser.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
#COST
cost = browser.find_element(By.NAME, 'unitCost')
actual_value = cost.get_attribute("value")
expected_value = "111.00"
assert actual_value == expected_value, f"Product's cost doesn't match after product updating. Expected: {expected_value}, Actual: {actual_value}"
print("Product's cost matches after product updating.")
time.sleep(1)
#COMPARE_AT_PRICE
compare = browser.find_element(By.NAME, 'compareAtPrice')
actual_value = compare.get_attribute("value")
expected_value = "222.00"
assert actual_value == expected_value, f"Product's compare-at price doesn't match after product updating. Expected: {expected_value}, Actual: {actual_value}"
print("Product's compare-at price matches after product updating.")
time.sleep(1)
#PRICE
price = browser.find_element(By.NAME, 'price')
actual_value = price.get_attribute("value")
expected_value = "333.00"
assert actual_value == expected_value, f"Product's price doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Product's price matches after product updating.")
time.sleep(1)
browser.execute_script("window.scrollBy(0, 300);")

#Navigate to inventory and verify it's quantity in Shop Location
element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/div/button/div/div[1]/p')
actual_value = element.text
expected_value = '10'
assert actual_value == expected_value, f"Quantiy in Shop location was not sync after product updating. Expected: {expected_value}, Actual: {actual_value}"
print("Quantity in Shop location was sync successfully after product updating.")
#Verify quantity in Germany Warehouse Location
element = browser.find_element(By.XPATH, '//*[@id="AppFrameMain"]/div/div/div[2]/form/div/div[1]/div[4]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/button/div/div[1]/p')
actual_value = element.text
expected_value = '10'
assert actual_value == expected_value, f"Quantiy in Germany Warehouse location was not sync after product updating. Expected: {expected_value}, Actual: {actual_value}"
print("Quantity in Germany Warehouse location was sync successfully after product updating.")

time.sleep(5)

#VERIFY THAT "SELENIUM" MANUAL COLLECTION SUCCESSFULLY UPDATED IN CONNECTED STORE
#Get Selenium in search collections
browser.get("https://admin.shopify.com/store/ivan-dev-store-2/collections?selectedView=all&query=selenium")
time.sleep(3)
#Click on 1st element in table
browser.find_element(By.CLASS_NAME, "Polaris-IndexTable__TableRow_1a85o").click()
time.sleep(4)
#Verify collection's title in connected store
title = browser.find_element(By.NAME, 'title')
actual_value = title.get_attribute("value")
expected_value = "UPDATED_SELENIUM_COLLECTION_TEST_TITLE"
assert actual_value == expected_value, f"Collection's title doesn't match. Expected: {expected_value}, Actual: {actual_value}"
print("Collection's title matches after updating.")
time.sleep(1)
#Verify collection's description in connected store
browser.switch_to.frame('collection-description_ifr')
description = browser.find_element(By.ID, "tinymce")
actual_text = description.text
expected_text = 'SELENIUMTEST_UPDATED'
assert actual_text == expected_text, f"Collection's description doesn't match after updating. Expected: {expected_value}, Actual: {actual_value}"
print("Collection's description matches after updating.")
time.sleep(1)
browser.switch_to.default_content()
#Verify that collection's image was synced in connected store
try:
    element = browser.find_element(By.XPATH, "//img[@class='mXwfQ']")
    src_attribute_value = element.get_attribute("src")
    search_word = 'tshirt'

    if search_word in src_attribute_value:
        print(Fore.GREEN + f'Image was updated successfully "{search_word}".')
    else:
        print(Fore.RED + f'Image was not updated successfully "{search_word}".')

except NoSuchElementException:
    print(Fore.RED + 'Image doesnt exist.')

finally:
    print(Style.RESET_ALL)



time.sleep(20)