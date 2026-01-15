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
        response.raise_for_status()
        return response.json()
