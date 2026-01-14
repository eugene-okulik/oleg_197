import requests
import faker
import random

from test_api_oleg_197.endpoints.endpoints import Endpoints


class CreatePost:
    fake = faker.Faker()
    sizes = ['XS', 'S', 'M', 'L', 'XL', 'AVERAGE', 'UNBELIEVABLE']

    def create(self):
        body = {
            'name': self.fake.name(),
            'data': {
                'color': self.fake.color_name(),
                'size': random.choice(self.sizes)
            }
        }
        response = requests.post(Endpoints.POST_URL, json=body)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        print(f'Объект создан: {response.text}')
        return response.json()['id']

    def create_with_name(self, name):
        body = {
            'name': name,
            'data': {
                'color': self.fake.color_name(),
                'size': random.choice(self.sizes)
            }
        }
        response = requests.post(Endpoints.POST_URL, json=body)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        print(f'Объект создан с именем "{name}": {response.text}')
        return response.json()['id']