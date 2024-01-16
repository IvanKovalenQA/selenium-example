import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://obliged.app/'
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get(base_url)
browser.maximize_window()
time.sleep(3)
button = browser.find_element(By.XPATH, "//*[text()='Accept']")
button.click()
browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/a[1]").click()
time.sleep(3)
button = browser.find_element(By.XPATH, "//*[text()='Accept']")
button.click()
time.sleep(3)
browser.find_element(By.ID, "name").send_keys("EGNSELENIUMCOMPANY")
#browser.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/button").click()
#time.sleep(3)
#file_path = '//users/user/Downloads/renis.jpeg'
#time.sleep(1)
##pyautogui.write(file_path)
#time.sleep(1)
#pyautogui.press('enter')
#time.sleep(2)
#pyautogui.press('enter')
#time.sleep(2)
browser.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[3]/button").click()
browser.find_element(By.ID, "employee_name").send_keys("Johnottan")
browser.find_element(By.ID, "employee_last_name").send_keys("Wick")
time.sleep(2)
element = browser.find_element(By.ID, "employee_country")
element.click()
select = Select(element)
select.select_by_value('23')
browser.execute_script("arguments[0].dispatchEvent(new Event('input'))", element)
time.sleep(2)
adress = browser.find_element(By.ID, "employee_address")
adress.click()
adress.send_keys('Baskent')
time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/button').click()
time.sleep(20)





