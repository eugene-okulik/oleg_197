import requests

from test_api_oleg_197.endpoints.endpoints import Endpoints


class PatchObj:
    def patch(self, post_id, name=None, data=None):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        body = {}
        if name is not None:
            body["name"] = name
        if data is not None:
            body["data"] = data

        if not body:
            raise ValueError('Для PATCH-запроса необходимо указать хотя бы одно из полей: "name" или "data"')

        response = requests.patch(url, json=body)
        assert response.status_code == 200, f'Ожидался статус 200, получен: {response.status_code}'
        return response.json()

    def assert_patch(self, post_id, name=None, data=None, expected_name=None, expected_data=None):
        updated = self.patch(post_id, name, data)
        if expected_name is not None:
            assert updated['name'] == expected_name, f"Имя: {updated['name']} != {expected_name}"
        if expected_data is not None:
            assert updated['data'] == expected_data, f"Данные: {updated['data']} != {expected_data}"
        return updated
