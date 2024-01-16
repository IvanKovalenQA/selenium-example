import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

base_url = 'https://obliged.app/'
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get(base_url)

browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/div/span/a").click()
time.sleep(1)
browser.find_element(By.ID,"name").send_keys("Ivan")
time.sleep(1)
browser.find_element(By.ID,"email").send_keys("ivan@egnition.io")
time.sleep(1)
browser.find_element(By.ID,"password").send_keys("12345678")
time.sleep(1)
browser.find_element(By.ID,"password_confirmation").send_keys("12345678")
time.sleep(2)
browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/form/div[5]/span/button").click()
time.sleep(2)
browser.quit()



