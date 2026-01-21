import allure
import requests

from test_api_oleg_197.endpoints.endpoints import BaseApi


class PutObj(BaseApi):
    url = 'http://objapi.course.qa-practice.com/object/{}'

    @allure.step('Полное обновление объекта (PUT)')
    def put(self, post_id, name=None, data=None):
        url = self.url.format(post_id)
        body = {
            "name": name,
            "data": data
        }
        self.response = requests.put(url, json=body)
        self.assert_status_code()
        return self.response

    @allure.step('Проверяем полное обновление объекта (PUT)')
    def assert_put(self, name, data):
        self.assert_fields(name=name, data=data)
