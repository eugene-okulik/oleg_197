from test_ui_oleg_197_pw.pages.base_page import BasePage
from test_ui_oleg_197_pw.pages.locators.product_page_locators import ADD_TO_CART_BTN


class ProductPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7'

    def add_to_cart(self):
        self.find_and_click(ADD_TO_CART_BTN)
