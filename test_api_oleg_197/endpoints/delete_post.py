import requests

from test_api_oleg_197.endpoints.endpoints import Endpoints


class DeletePost:
    def delete(self, post_id):
        delete_url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.delete(delete_url)
        if response.status_code == 200:
            print(f'Объект {post_id} удален')
        else:
            print(f'Warning: не удалось удалить объект {post_id}')
