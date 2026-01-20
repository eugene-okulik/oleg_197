import allure
import requests

from test_api_oleg_197.endpoints.endpoints import BaseAsserts


class PutObj():
    url = 'http://objapi.course.qa-practice.com/object/{}'

    def __init__(self):
        self.response = None

    @allure.step('Полное обновление объекта (PUT)')
    def put(self, post_id, name=None, data=None):
        url = self.url.format(post_id)
        body = {
            "name": name,
            "data": data
        }
        self.response = requests.put(url, json=body)
        BaseAsserts.assert_status_code(self.response)
        return self.response

    @allure.step('Проверяем полное обновление объекта (PUT)')
    def assert_put(self, name, data):
        BaseAsserts.assert_fields(self.response.json(), name=name, data=data)
