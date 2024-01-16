import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

base_url = 'https://fyl.vqr.mybluehost.me/'
expected_title = 'Homepage - Ekinox - Welcome'

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get(base_url)
assert expected_title in browser.title
assert base_url in browser.current_url
time.sleep(5)
browser.find_element(By.LINK_TEXT, 'EVENTS').click()
time.sleep(5)
browser.find_element(By.LINK_TEXT, 'PAST SHOWS').click()
dropdown = Select(browser.find_element(By.ID, 'artists_filter'))
# dropdown.select_by_visible_text('DJ Capital')
# time.sleep(5)
dropdown.select_by_value('1210')
# dropdown.select_by_index(6)
time.sleep(3)