import faker
import random


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

    def generate_body(self, name=None):
        if name is None:
            name = self.fake.name()

        body = {
            'name': name,
            'data': {
                'color': self.fake.color_name(),
                'size': random.choice(self.sizes)
            }
        }
        return body
