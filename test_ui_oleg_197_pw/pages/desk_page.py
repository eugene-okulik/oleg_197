import re

import allure

from test_ui_oleg_197_pw.pages.base_page import BasePage
from test_ui_oleg_197_pw.pages.locators.desk_page_locators import PRODUCT_CONTAINER, PRODUCT_CARD, SORT_BY_BTN, SORT_BY_NAME
from test_ui_oleg_197_pw.pages.locators.main_page_locators import CATEGORIES_BTN, DESKS_BTN


class DeskPage(BasePage):
    page_url = '/shop/category/desks-1'

    @allure.step('Переходим на страницу /shop/category/desks-1')
    def go_to_desk_page(self):
        with allure.step(f'Наводимся на элемент {CATEGORIES_BTN}'):
            self.page.locator(CATEGORIES_BTN).hover()
            self.find_and_click(DESKS_BTN)

    @allure.step('Выбираем сортировку Name A-Z в списке')
    def sorted_asc(self):
        self.find_and_click(SORT_BY_BTN)
        self.find_and_click(SORT_BY_NAME)

    @allure.step('Собираем список товаров со страницы')
    def products_name_from_page(self):
        product_elements = self.wait_for_products_loaded()
        product_names = [
            re.sub(r'\s*\$\s*[\d,]+\.?\d*\s*$', '',
                   re.sub(r'\s+', ' ', element.text_content().strip()).lower())
            for element in product_elements
            if element.text_content() and element.text_content().strip()
        ]
        return product_names

    @allure.step('Получаем список товаров')
    def wait_for_products_loaded(self):
        self.find_visible(PRODUCT_CONTAINER)
        products = self.page.locator(PRODUCT_CARD).all()
        return products
