import requests

from test_api_oleg_197.endpoints.endpoints import Endpoints


class PutObj:
    def put(self, post_id, name, data):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        body = {
            "name": name,
            "data": data
        }
        response = requests.put(url, json=body)
        assert response.status_code == 200, f'Ожидался статус 200, получен: {response.status_code}'
        return response.json()

    def assert_put(self, post_id, name, data):
        updated = self.put(post_id, name, data)
        assert updated['name'] == name, f"Имя не совпадает: {updated['name']} != {name}"
        assert updated['data'] == data, f"Данные не совпадают: {updated['data']} != {data}"
        return updated
