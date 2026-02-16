import random

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


def test_step_1(driver, wait):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    select = driver.find_element(By.XPATH, '//select[@id="id_choose_language"]')
    select = Select(select)
    value = [1, 2, 3, 4, 5]
    random_value = random.choice(value)
    select.select_by_value(str(random_value))

    selected_value = select.first_selected_option.text
    print(f"Выбрано: {selected_value}")

    submit_button = driver.find_element(By.XPATH, '//input[@id="submit-id-submit"]')
    submit_button.click()

    result_element = wait.until(
        ec.visibility_of_element_located((By.XPATH, '//p[@id="result-text"]'))
    )

    result_text = result_element.text
    print(f'Результат: {result_text}')

    assert selected_value in result_text, f'Ожидалось "{selected_value}", получено "{result_text}"'


def test_step_2(driver, wait):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, '//div[@id="start"]/button')
    start_button.click()

    result_element = wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@id="finish"]/h4')))
    result_text = result_element.text
    print(f'Появившийся текст: {result_text}')
    assert result_text == 'Hello World!', f'Ожидалось "Hello World!", получено "{result_text}"'
