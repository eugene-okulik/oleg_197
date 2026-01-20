import allure
import requests

from test_api_oleg_197.endpoints.endpoints import BaseAsserts


class PatchObj():
    url = 'http://objapi.course.qa-practice.com/object/{}'

    def __init__(self):
        self.response = None

    @allure.step('Частичное обновление объекта (PATCH)')
    def patch(self, post_id, name, data):
        url = self.url.format(post_id)
        body = {}
        if name is not None:
            body["name"] = name
        if data is not None:
            body["data"] = data
        if not body:
            raise ValueError('Для PATCH-запроса необходимо указать хотя бы одно из полей: "name" или "data"')

        self.response = requests.patch(url, json=body)
        BaseAsserts.assert_status_code(self.response)
        return self.response.json()

    @allure.step('Проверяем частичное обновление объекта (PATCH)')
    def assert_patch(self, expected_name=None, expected_data=None):
        if expected_name is not None:
            BaseAsserts.assert_fields(self.response.json(), name=expected_name)
        if expected_data is not None:
            BaseAsserts.assert_fields(self.response.json(), data=expected_data)
