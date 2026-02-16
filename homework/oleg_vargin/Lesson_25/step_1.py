import pytest
import faker

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_form(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    wait = WebDriverWait(driver, 10)
    input_text = faker.Faker().word()

    input_field = wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="id_text_string"]')))
    input_field.send_keys(input_text)
    input_field.send_keys(Keys.ENTER)

    wait.until(ec.text_to_be_present_in_element(
        (By.XPATH, '//p[@id="result-text"]'), input_text))

    result_element = driver.find_element(By.XPATH, '//p[@id="result-text"]')

    print(f'Результат: {result_element.text}')

    assert result_element.text == input_text
