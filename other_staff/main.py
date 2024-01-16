from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://www.ebay.com/'
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
def wait_and_select_dropdown_by_name(seconds, name, text):
    dropdown = Select(
        WebDriverWait(browser, seconds).until(EC.element_to_be_clickable(browser.find_element(By.NAME, name))))
    dropdown.select_by_visible_text(text)
def verify_page_title(seconds, title):
    WebDriverWait(browser, seconds).until(EC.title_contains(title))
    assert title in browser.title
def wait_and_click_link(browser, link_text):
    wait = WebDriverWait(browser, 3)
    element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
    element.click()

#Navigate to eBay and verify title
browser.get(base_url)
verify_page_title(5, "Electronics, Cars, Fashion, Collectibles & More | eBay")
#Navigate to "eBay Motors".Verify title.
wait_and_click_link(browser, "Motors")
wait_and_click_link(browser, "eBay Motors")
verify_page_title(5, "eBay Motors: Auto Parts and Vehicles | eBay")
#Select desired values from dropdown menus.
wait_and_select_dropdown_by_name(5, "Make", "Aston Martin")
wait_and_select_dropdown_by_name(5, "Model", "DB11")
#Clearing a zip code field and filling it with valid values.
zip_code = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "_stpos")))
zip_code.clear()
zip_code.send_keys("07400")
#Click "Find Vehicles" and verify new page's title.
browser.find_element(By.CSS_SELECTOR, '.btn.btn--primary.motors-finder__find-btn').click()
verify_page_title(5, "Aston Martin DB11 in Cars & Trucks for sale | eBay")

browser.quit()