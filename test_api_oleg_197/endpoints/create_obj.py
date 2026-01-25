import requests
import allure

from test_api_oleg_197.endpoints.endpoints import BaseApi


class CreateObj(BaseApi):

    url = 'http://objapi.course.qa-practice.com/object'

    def create_base(self, name=None):
        body = self.generate_body(name=name)
        self.response = requests.post(self.url, json=body)
        self.assert_status_code()

        if name is None:
            with allure.step(f'Объект создан: {self.response.text}'):
                pass
        else:
            with allure.step(f'Объект создан с именем "{name}": {self.response.text}'):
                pass

        return self.response.json()['id']

    @allure.step('Создаём объект')
    def create(self):
        return self.create_base()

    @allure.step('Создаём объект с именем {name}')
    def create_with_name(self, name):
        return self.create_base(name=name)
