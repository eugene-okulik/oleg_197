import re

import allure
from playwright.sync_api import Page, expect, Locator

from test_ui_oleg_197_pw.pages.locators.main_page_locators import SHOP_CART, OFFICE_DESIGN_SOFTWARE, TOAST_HEADER
from test_ui_oleg_197_pw.pages.locators.product_page_locators import OFFICE_DESIGN_SOFTWARE_TEXT


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Открываем главнцую страницу')
    def open_base_page(self):
        url = self.base_url
        self.page.goto(url)

    @allure.step('Открываем страницу {{page_url}}')
    def open_page_url(self):
        url = f'{self.base_url}{self.page_url}'
        self.page.goto(url)

    def find(self, locator):
        return self.page.locator(locator)

    @allure.step('Ищем элемент {locator} и переходим кликом по нему')
    def find_and_click(self, locator):
        return self.page.locator(locator).click()

    def find_visible(self, locator) -> Locator:
        return self.page.wait_for_selector(locator)

    @allure.step('Проверяем, что page_url соответсвует текущему url')
    def assert_page_url_in_current_url(self):
        expect(self.page).to_have_url(re.compile(f'.*{self.page_url}.*'))

    def presence_of_element_located(self, locator):
        self.page.wait_for_selector(locator)
        return self.page.locator(locator)

    @allure.step('Извлекаем названия товаров')
    def get_product_names(self, locator):
        return self.page.locator(locator).all_text_contents()

    @allure.step('Переходим в корзину товаров')
    def click_shop_cart(self):
        self.find_and_click(SHOP_CART)

    @allure.step('Переходим на страницу товара Office Design Software')
    def click_office_design_software(self):
        self.find_and_click(OFFICE_DESIGN_SOFTWARE)

    @allure.step('Сравниваем отсортированные списки товаров')
    def assert_sorted(self, product_names):
        sorted_names = sorted(product_names)
        assert product_names == sorted_names, 'Товары не отсортированы по названию (A-Z)!'

    @allure.step('Проверяем наличие товаров на странице')
    def assert_len_products(self, products):
        product_count = len(products)
        assert product_count > 0, f'На странице не отображены товары! Найдено: {product_count} товаров'

    @allure.step('Проверяем название продукта')
    def assert_product_name(self, text):
        product = self.find(OFFICE_DESIGN_SOFTWARE_TEXT)
        expect(product).to_have_text(text)

    @allure.step('Проверка появления TOAST_HEADER после добавления товара в корзину')
    def assert_toast_header(self):
        expect(self.page.locator(TOAST_HEADER)).to_be_visible()
