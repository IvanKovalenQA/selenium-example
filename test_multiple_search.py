import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize("make, model, postal_code, condition",
                         [
                             ('BMW', 'M4', '20180', 'New & Used'),
                             ('Bentley', 'Continental', '20003', 'Used'),
                             ('Land Rover', 'Range Rover Sport', '00001', 'New')
                         ])
@pytest.mark.regressiontest2
def test_ebay_search_vehicle_multiple(browser, make, model, postal_code, condition):
    base_url = 'https://www.ebay.com/'
    expected_title = 'Electronics, Cars, Fashion, Collectibles & More | eBay'

    browser.get(base_url)
    assert expected_title in browser.title
    assert base_url in browser.current_url
    browser.find_element(By.LINK_TEXT, 'Motors').click()

    make_dropdown = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable(browser.find_element(By.XPATH, "//select[@aria-label='All Makes']"))))
    make_dropdown.select_by_visible_text(make)

    model_dropdown = Select(WebDriverWait(browser, 7).until(EC.element_to_be_clickable(browser.find_element(By.CSS_SELECTOR, "select[aria-label='All Models']"))))
    model_dropdown.select_by_visible_text(model)

    zip_code = WebDriverWait(browser, 6).until(EC.element_to_be_clickable(browser.find_element(By.NAME, '_stpos')))
    zip_code.clear()
    zip_code.send_keys(postal_code)

    condition_dropdown = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable(browser.find_element(By.CSS_SELECTOR, "select[aria-label='Condition']"))))
    condition_dropdown.select_by_visible_text(condition)

    find_button = WebDriverWait(browser, 6).until(EC.element_to_be_clickable(browser.find_element(By.XPATH, "//button[text()='Find Vehicle']")))
    find_button.click()

    WebDriverWait(browser, 5).until(EC.title_contains(model))
    assert model in browser.title