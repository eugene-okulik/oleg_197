import allure
import requests
import faker
import random

from test_api_oleg_197.endpoints.endpoints import BaseAsserts


class CreateObj():
    fake = faker.Faker()
    sizes = ['XS', 'S', 'M', 'L', 'XL', 'AVERAGE', 'UNBELIEVABLE']
    url = 'http://objapi.course.qa-practice.com/object'

    def __init__(self):
        self.response = None

    @allure.step('Создаём объект')
    def create(self):
        body = {
            'name': self.fake.name(),
            'data': {
                'color': self.fake.color_name(),
                'size': random.choice(self.sizes)
            }
        }
        self.response = requests.post(self.url, json=body)
        BaseAsserts.assert_status_code(self.response)
        with allure.step(f'Объект создан: {self.response.text}'):
            pass
        return self.response.json()['id']

    @allure.step('Создаём объект с именем {name}')
    def create_with_name(self, name):
        body = {
            'name': name,
            'data': {
                'color': self.fake.color_name(),
                'size': random.choice(self.sizes)
            }
        }
        self.response = requests.post(self.url, json=body)
        BaseAsserts.assert_status_code(self.response)
        with allure.step(f'Объект создан с именем "{name}": {self.response.text}'):
            pass
        return self.response.json()['id']
