import requests

from test_api_oleg_197.endpoints.endpoints import Endpoints


class PutPost:
    def put(self, post_id, name, data):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        body = {
            "name": name,
            "data": data
        }
        response = requests.put(url, json=body)
        response.raise_for_status()
        return response.json()
