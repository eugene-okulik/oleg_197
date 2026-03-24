import allure


@allure.feature('Категория столы')
@allure.story('page_url /shop/category/desks-1')
class TestDeskPage:

    @allure.title('Проверка открытия страницы /shop/category/desks-1 с главной страницы')
    def test_open_desk_page_from_base_page(self, desk_page):
        desk_page.open_base_page()
        desk_page.go_to_desk_page()
        desk_page.assert_page_url_in_current_url()

    @allure.title('Проверка наличия товаров')
    def test_page_loads_and_products_displayed(self, desk_page):
        desk_page.open_page_url()
        products = desk_page.wait_for_products_loaded()
        desk_page.assert_len_products(products)

    @allure.title('Проверка сортировки товаров')
    def test_products_sorted_by_name_ascending(self, desk_page):
        desk_page.open_page_url()
        desk_page.sorted_asc()
        product_names = desk_page.products_name_from_page()
        desk_page.assert_sorted(product_names)
