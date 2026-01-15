import requests

from test_api_oleg_197.endpoints.endpoints import Endpoints


class DeleteObj:
    def delete(self, post_id):
        delete_url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.delete(delete_url)
        assert response.status_code == 200, f'Ожидался статус 200, получен: {response.status_code}'
        print(f'Объект {post_id} удален')
