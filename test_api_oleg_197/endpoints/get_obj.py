import requests

from test_api_oleg_197.endpoints.endpoints import Endpoints


class GetObj:
    def get(self, post_id):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


    def assert_deleted(self, post_id):
        url = Endpoints.OBJECT_URL_TEMPLATE.format(post_id)
        response = requests.get(url)
        if response.status_code == 404:
            print(f'При поиске объект {post_id} после удаления объект {post_id} не найден в БД')
        else:
            print(f'Warning: объект {post_id} найден в БД')