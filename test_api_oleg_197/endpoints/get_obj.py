import allure
import requests

from test_api_oleg_197.endpoints.endpoints import BaseAsserts


class GetObj():
    url = 'http://objapi.course.qa-practice.com/object/{}'

    def __init__(self):
        self.response = None

    @allure.step('Открываем объект')
    def get(self, post_id):
        self.response = requests.get(self.url.format(post_id))
        BaseAsserts.assert_status_code(self.response)
        return self.response.json()

    @allure.step('Повторная проверка удаления')
    def assert_code(self, post_id, expected_code: int):
        self.response = requests.get(self.url.format(post_id))
        actual_code = self.response.status_code
        assert actual_code == expected_code, f'Ожидался статус {expected_code}, получен: {actual_code}'
        if expected_code == 404:
            with allure.step(f'Объект {post_id} не найден — успешно удалён'):
                pass
        else:
            with allure.step(f'Объект {post_id} доступен (статус: {actual_code})'):
                pass

    @allure.step('Проверка ожидаемого поля')
    def assert_object_fields(self, post_id, **expected_fields):
        obj = self.get(post_id)
        BaseAsserts.assert_fields(obj, **expected_fields)
