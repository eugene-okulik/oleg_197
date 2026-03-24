import allure
from playwright.sync_api import expect

from test_ui_oleg_197_pw.pages.base_page import BasePage
from test_ui_oleg_197_pw.pages.locators.main_page_locators import CONTINUE_SHOPPING_BTN
from test_ui_oleg_197_pw.pages.locators.shop_cart_locators import CHECKOUT_BTN, REMOVE_BTN, PRODUCT_PRICE, \
    TOTAL_UNTAXED, TOTAL_TAXES, \
    ORDER_TOTAL


class CartPage(BasePage):
    page_url = '/shop/cart'

    @allure.step('Сравнение цен продукта')
    def assert_price_comparison(self):
        product_price_text = self.page.locator(PRODUCT_PRICE).inner_text()
        total_untaxed_text = self.page.locator(TOTAL_UNTAXED).inner_text()
        total_taxed_text = self.page.locator(TOTAL_TAXES).inner_text()
        order_total_text = self.page.locator(ORDER_TOTAL).inner_text()

        product_price = float(self.clean_price(product_price_text))
        total_untaxed = float(self.clean_price(total_untaxed_text))
        total_taxed = float(self.clean_price(total_taxed_text))
        order_total = float(self.clean_price(order_total_text))

        assert product_price == total_untaxed, (
            f'Цена продукта ({product_price}) не равна цене без налога ({total_untaxed})'
        )

        expected_total = total_untaxed + total_taxed
        assert order_total == expected_total, (
            f'Конечная цена ({order_total}) отличается от суммы цены без налога ({total_untaxed}) '
            f'и налога ({total_taxed}). Ожидалось: {expected_total}'
        )

    def clean_price(self, price_text: str) -> str:
        import re
        cleaned = re.sub(r'[^\d.-]', '', price_text)
        return cleaned

    @allure.step('Добавляем продукт в корзину')
    def add_to_cart(self, item_locator, cart_locator):
        self.page.locator(item_locator).hover()
        # self.actions.move_to_element(self.find(item_locator)).perform()
        self.find_and_click(cart_locator)
        self.find_and_click(CONTINUE_SHOPPING_BTN)

    @allure.step('Переход по кнопке Checkout')
    def click_checkout(self):
        self.find_and_click(CHECKOUT_BTN)

    @allure.step('Удаляем все товары из корзины')
    def delete_all_products(self):
        buttons = self.page.locator(REMOVE_BTN).all()

        for index, button in enumerate(buttons):
            with allure.step(f'Нажимаем кнопку удаления товара {index + 1}'):
                try:
                    button.click(timeout=5000)
                except Exception as e:
                    print(f'Ошибка при клике на кнопку {index + 1}: {e}')
                    continue
