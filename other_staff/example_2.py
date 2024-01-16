import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

#this is my second test
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get("https://www.google.com")
print(browser.title)
time.sleep(2)
#browser.refresh()
# time.sleep(2)
# browser.get("https://www.ebay.com")
# time.sleep(2)
# browser.back()
# time.sleep(2)
# browser.forward()
# time.sleep(2)
browser.quit()