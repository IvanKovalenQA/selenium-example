import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize("year, make, model, trim", [
    ('2020', 'BMW', '420i Gran Coupe', 'Executive Hatchback 4-Door'),
    ('2024', 'Lexus', 'RX350', 'Luxury Sport Utility 4-Door'),
    ('1896', 'Duryea', 'Duryea', 'Base')
])
@pytest.mark.regressiontest5
def test_ebay_search_motors_multiple(browser, year, make, model, trim):
    base_url = 'https://www.ebay.com/'
    expected_title = 'Electronics, Cars, Fashion, Collectibles & More | eBay'


    browser.get(base_url)
    assert expected_title in browser.title
    assert base_url in browser.current_url
    browser.find_element(By.LINK_TEXT, 'Motors').click()

    year_dropdown = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Year'))))
    year_dropdown.select_by_visible_text(year)

    make_dropdown = Select(WebDriverWait(browser, 7).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Make'))))
    make_dropdown.select_by_visible_text(make)

    model_dropdown = Select(WebDriverWait(browser, 6).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Model'))))
    model_dropdown.select_by_visible_text(model)

    trim_dropdown = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Trim'))))
    trim_dropdown.select_by_visible_text(trim)

    find_button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(browser.find_element(By.XPATH, "//button[@type='submit'][text()='Find Parts']")))
    find_button.click()

    WebDriverWait(browser, 5).until(EC.title_contains('My Garage'))
    assert 'My Garage' in browser.title
    assert 'mygarage' in browser.current_url