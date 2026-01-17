import requests

from test_api_oleg_197.helpers import assert_fields
from test_api_oleg_197.endpoints.endpoints import Endpoints


class GetObj():
    def get(self, post_id):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.get(url)
        return response.json()

    def assert_code(self, post_id, expected_code: int):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.get(url)
        actual_code = response.status_code
        assert actual_code == expected_code, f'Ожидался статус {expected_code}, получен: {actual_code}'
        if expected_code == 404:
            print(f'Объект {post_id} не найден — успешно удалён')
        else:
            print(f'Объект {post_id} доступен (статус: {actual_code})')

    def assert_object_fields(self, post_id, **expected_fields):
        obj = self.get(post_id)
        assert_fields(obj, **expected_fields)
