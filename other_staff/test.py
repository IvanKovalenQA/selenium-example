import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

#Open the browser.Navigate to Soundrise site.
browser.get('http://ec2-35-77-8-202.ap-northeast-1.compute.amazonaws.com/')
time.sleep(5)

#Verify that Home Page is displayed.
page_title = browser.title
expected_title = 'IT Simple – Just another WordPress site'
if page_title == expected_title:
    print("Home page is displaying")
else:
    print("Home Page is not displaying")

#Verify that SoundRise company logo is displayed at the top left corner of the Home Page.
try:
    element = browser.find_element(By.XPATH, ('//*[@id="menu-main-menu"]/li[1]/a/img'))
    if element.is_displayed():
        print("Company logo is displaying at the top left corner of the Home Page")
    else:
        print("Company logo is not displaying at the top left corner of the Home Page")
except NoSuchElementException:
    print("Element is not found")

#Click on "ARTISTS" link from the Top Menu.
browser.find_element(By.XPATH, '//*[@id="menu-item-1397"]/a').click()
time.sleep(2)

#Verify that "ARTIST" page is displayed.
page_title = browser.title
expected_title = 'Artists Grid – Fullwidth – IT Simple'
if page_title == expected_title:
    print("Artists page is displaying")
else:
    print("Artists page is not displaying")

#Verify that SoundRise company logo is displayed at the top left corner of the "ARTIST" page.
try:
    element = browser.find_element(By.XPATH, ('//*[@id="menu-main-menu"]/li[1]/a/img'))
    if element.is_displayed():
        print("Company logo is displaying at the top left corner of the Artists Page")
    else:
        print("Company logo is not displaying at the top left corner of the Artists Page")
except NoSuchElementException:
    print("Element is not found")

#Click on "RELEASES" link from the Top Menu.
browser.find_element(By.XPATH, '//*[@id="menu-item-1396"]/a').click()
time.sleep(2)

#Verify that "RELEASES" page is displayed.
page_title = browser.title
expected_title = 'Releases Grid – Boxed – IT Simple'
if page_title == expected_title:
    print("Releases page is displaying")
else:
    print("Releases page is not displaying")

#Verify that SoundRise company logo is displayed at the top left corner of the "RELEASES" page.
try:
    element = browser.find_element(By.XPATH, ('//*[@id="menu-main-menu"]/li[1]/a/img'))
    if element.is_displayed():
        print("Company logo is displaying at the top left corner of the Releases Page")
    else:
        print("Company logo is not displaying at the top left corner of the Releases Page")
except NoSuchElementException:
    print("Element is not found")

#Click on "EVENTS" link from the Top Menu.
browser.find_element(By.XPATH, '//*[@id="menu-item-1134"]/a').click()
time.sleep(2)

#Verify that "EVENTS" page is displayed.
page_title = browser.title
expected_title = 'Upcoming Shows – IT Simple'
if page_title == expected_title:
    print("Events page is displaying")
else:
    print("Events page is not displaying")

#Verify that SoundRise company logo is displayed at the top left corner of the "EVENTS" page.
try:
    element = browser.find_element(By.XPATH, ('//*[@id="menu-main-menu"]/li[1]/a/img'))
    if element.is_displayed():
        print("Company logo is displaying at the top left corner of the Events Page")
    else:
        print("Company logo is not displaying at the top left corner of the Events Page")
except NoSuchElementException:
    print("Element is not found")

#Click on "CONTACT" link from the Top Menu.
browser.find_element(By.XPATH, '//*[@id="menu-item-42"]/a').click()
time.sleep(2)

#Verify that "CONTACT" page is displayed.
page_title = browser.title
expected_title = 'Contact – IT Simple'
if page_title == expected_title:
    print("Contact page is displaying")
else:
    print("Contact page is not displaying")

#Verify that SoundRise company logo is displayed at the top left corner of the "CONTACT" page.
try:
    element = browser.find_element(By.XPATH, ('//*[@id="menu-main-menu"]/li[1]/a/img'))
    if element.is_displayed():
        print("Company logo is displaying at the top left corner of the Contact Page")
    else:
        print("Company logo is not displaying at the top left corner of the Contact Page")
except NoSuchElementException:
    print("Element is not found")

#Click on "ELEMENTS" link from the Top Menu.
browser.find_element(By.XPATH, '//*[@id="menu-item-2539"]/a').click()
time.sleep(2)

#Verify that "ELEMENTS" page is displayed.
page_title = browser.title
expected_title = 'Elements – IT Simple'
if page_title == expected_title:
    print("Elements page is displaying")
else:
    print("Elements page is not displaying")
#!"ELEMENTS" PAGE IS NOT DISPLAYED!
