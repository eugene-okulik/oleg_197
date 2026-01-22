import faker
import random
import requests
import allure


class BaseApi:
    fake = faker.Faker()
    sizes = ['XS', 'S', 'M', 'L', 'XL', 'AVERAGE', 'UNBELIEVABLE']

    def __init__(self):
        self.response = None

    def assert_fields(self, **expected_fields):
        for field, expected_value in expected_fields.items():
            actual_value = self.response.json().get(field)
            assert actual_value == expected_value, \
                f'Поле {field}: ожидалось {expected_value}, получено {actual_value}'

    def assert_status_code(self, expected_status=200):
        assert self.response.status_code == expected_status, \
            f'Ожидался статус {expected_status}, получен: {self.response.status_code}'

    def assert_update(self, expected_name=None, expected_data=None):
        if expected_name is not None:
            assert self.response['name'] == expected_name, f'Имя: {self.response["name"]} != {expected_name}'
        if expected_data is not None:
            assert self.response['data'] == expected_data, f'Данные: {self.response["data"]} != {expected_data}'

    def create_base(self, name=None):
        generate_name = self.fake.name()

        if name is None:
            name = generate_name

        body = {
            'name': name,
            'data': {
                'color': self.fake.color_name(),
                'size': random.choice(self.sizes)
            }
        }
        self.response = requests.post(self.url, json=body)
        self.assert_status_code()

        if name == generate_name:
            with allure.step(f'Объект создан: {self.response.text}'):
                pass
        else:
            with allure.step(f'Объект создан с именем "{name}": {self.response.text}'):
                pass

        return self.response.json()['id']
