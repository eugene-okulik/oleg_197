import requests

from test_api_oleg_197.endpoints.base_obj import BaseObj
from test_api_oleg_197.endpoints.endpoints import Endpoints


class PatchObj(BaseObj):
    def _make_request(self, post_id, name=None, data=None):
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
