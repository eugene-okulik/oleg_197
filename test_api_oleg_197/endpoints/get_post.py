import requests

from test_api_oleg_197.endpoints.endpoints import Endpoints


class GetPost:
    def get(self, post_id):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()