import pytest

from test_ui_oleg_197_pw.pages.base_page import BasePage
from test_ui_oleg_197_pw.pages.cart_page import CartPage
from test_ui_oleg_197_pw.pages.desk_page import DeskPage
from test_ui_oleg_197_pw.pages.locators.main_page_locators import CUSTOMIZABLE_DESK, CART_BTN_FOR_CUSTOMIZABLE_DESK, \
    TOAST_HEADER, \
    OFFICE_DESIGN_SOFTWARE
from test_ui_oleg_197_pw.pages.shipping_page_locators import ShippingPage
from test_ui_oleg_197_pw.pages.locators.shop_cart_locators import EMPTY_CART
from test_ui_oleg_197_pw.pages.product_page import ProductPage


@pytest.fixture
def base_page(page):
    return BasePage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def shipping_page(page):
    return ShippingPage(page)


@pytest.fixture
def add_product_to_cart(base_page, cart_page):
    base_page.open_base_page()
    cart_page.add_to_cart(CUSTOMIZABLE_DESK, CART_BTN_FOR_CUSTOMIZABLE_DESK)
    base_page.find_visible(TOAST_HEADER)


@pytest.fixture
def del_all_product_at_cart(base_page, cart_page):
    cart_page.delete_all_products()
    base_page.find_visible(EMPTY_CART)


@pytest.fixture
def add_and_delete_product(add_product_to_cart, cart_page):
    yield
    cart_page.delete_all_products()
    cart_page.page.locator(EMPTY_CART)


@pytest.fixture
def desk_page(page):
    return DeskPage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def product_name(product_page):
    product_page.open_base_page()
    product = product_page.find(OFFICE_DESIGN_SOFTWARE)
    return product.inner_text()
