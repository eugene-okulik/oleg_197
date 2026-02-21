import pytest

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


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


@pytest.fixture
def actions(driver):
    return ActionChains(driver)


def test_add_to_cart_from_new_tab(driver, wait, actions):
    driver.get('http://testshop.qa-practice.com/')
    customizable_desk = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[content="Customizable Desk"]')))
    text = customizable_desk.text
    actions.key_down(Keys.CONTROL).click(customizable_desk).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    add_to_cart_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#add_to_cart')))
    add_to_cart_button.click()

    continue_shopping_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.btn-secondary')))
    continue_shopping_button.click()

    wait.until(ec.title_contains('Customizable Desk'))

    driver.close()
    driver.switch_to.window(tabs[0])

    main_cart = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.flex-shrink-0 [href="/shop/cart"]')))
    main_cart.click()

    customizable_desk_in_cart = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.d-inline')))

    assert text in customizable_desk_in_cart.text


def test_add_to_cart(driver, wait, actions):
    driver.get('http://testshop.qa-practice.com/')
    customizable_desk = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[content="Customizable Desk"]')))
    text = customizable_desk.text

    actions.move_to_element(customizable_desk).perform()

    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[value="12"] + [role="button"]'))).click()

    product = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'td> .product_display_name')))

    assert text in product.text
