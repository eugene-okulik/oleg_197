import requests

from test_api_oleg_197.endpoints.endpoints import Endpoints


class GetObj:
    def get(self, post_id):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.get(url)
        assert response.status_code == 200, f'Ожидался статус 200, получен: {response.status_code}'
        return response.json()

    def assert_deleted(self, post_id):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.get(url)
        assert response.status_code == 404, f'Объект {post_id} не был удалён'
        print(f'Объект {post_id} не найден — успешно удалён')

    def assert_name(self, post_id, expected_name):
        obj = self.get(post_id)
        assert obj['name'] == expected_name, f"Имя: ожидалось '{expected_name}', получено '{obj['name']}'"

    def assert_id(self, post_id):
        obj = self.get(post_id)
        assert obj['id'] == post_id, f"ID не совпадает: {obj['id']} != {post_id}"
