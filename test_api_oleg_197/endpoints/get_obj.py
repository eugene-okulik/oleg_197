import allure
import requests

from test_api_oleg_197.endpoints.endpoints import BaseApi


class GetObj(BaseApi):
    url = 'http://objapi.course.qa-practice.com/object/{}'

    @allure.step('Открываем объект')
    def get(self, post_id):
        self.response = requests.get(self.url.format(post_id))
        if self.response.status_code == 200:
            return self.response.json()
        else:
            return None

    @allure.step('Повторная проверка удаления')
    def assert_code(self, post_id, expected_code: int):
        self.get(post_id)
        actual_code = self.response.status_code
        self.assert_status_code(expected_code)
        if expected_code == 404:
            with allure.step(f'Объект {post_id} не найден — успешно удалён'):
                pass
        else:
            with allure.step(f'Объект {post_id} доступен (статус: {actual_code})'):
                pass

    @allure.step('Проверка ожидаемого поля')
    def assert_object_fields(self, post_id, **expected_fields):
        self.get(post_id)
        self.assert_fields(**expected_fields)
