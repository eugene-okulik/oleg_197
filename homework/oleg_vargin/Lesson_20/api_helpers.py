import requests
import faker
import random

fake = faker.Faker()

base_url = 'http://objapi.course.qa-practice.com/'

size = ['XS', 'S', 'M', 'L', 'XL', 'AVERAGE', 'UNBELIEVABLE']


def post():
    body = {
        'name': fake.name(),
        'data': {
            'color': fake.color_name(),
            'size': random.choice(size)
        }
    }
    post_url = base_url + 'object'
    response = requests.post(post_url, json=body)
    assert response.status_code == 200
    print(f'Объект создан: {response.text}')
    post_id = response.json()['id']
    return post_id


def delete(post_id):
    delete_url = f'{base_url}object/{post_id}'
    response = requests.delete(delete_url)
    if response.status_code == 200:
        print(f'Объект {post_id} удален')
    else:
        print(f'Warning: не удалось удалить объект {post_id}')
