import allure


@allure.feature('Страница товара')
@allure.story('page_url /shop/furn-9999-office-design-software-7')
class TestProductPage:

    @allure.title('Проверка открытия страницы /shop/furn-9999-office-design-software-7?category=9 с главной страницы')
    def test_open_product_page_from_base_page(self, base_page, product_page):
        base_page.open_base_page()
        base_page.click_office_design_software()
        product_page.assert_page_url_in_current_url()

    @allure.title('Проверка соответсвия названия продукта')
    def test_checking_product_name(self, product_page, product_name):
        text = product_name
        product_page.open_page_url()
        product_page.assert_product_name(text)

    @allure.title('Проверка добавления продукта в корзину')
    def test_add_to_cart(self, product_page):
        product_page.open_page_url()
        product_page.add_to_cart()
        product_page.assert_toast_header()
