import random
import requests
import faker
import pytest

fake = faker.Faker()

base_url = 'http://objapi.course.qa-practice.com/'

size = ['XS', 'S', 'M', 'L', 'XL', 'AVERAGE', 'UNBELIEVABLE']


@pytest.fixture(scope='session', autouse=True)
def session_setup_teardown():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(autouse=True)
def function_setup_teardown():
    print('\nbefore test')
    yield
    print('after test')


@pytest.fixture()
def post_and_delete():
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
    yield post_id
    delete_url = f'{base_url}object/{post_id}'
    response = requests.delete(delete_url)
    if response.status_code == 200:
        print(f'Объект {post_id} удален')
    else:
        print(f'Warning: не удалось удалить объект {post_id}')


@pytest.mark.critical
@pytest.mark.parametrize('name', [
    'test_1',
    'test_2',
    'test_3'
])
def test_post(name):
    body = {
        'name': name,
        'data': {
            'color': fake.color_name(),
            'size': random.choice(size)
        }
    }
    post_url = base_url + 'object'
    response = requests.post(post_url, json=body)
    print(f'Объект создан: {response.text}')

    assert response.status_code == 200
    obj_id = response.json()['id']
    print('Тест создания объекта пройден.')

    delete_resp = requests.delete(f'{base_url}object/{obj_id}')
    if delete_resp.status_code == 200:
        print(f'Oбъект {obj_id} удален')
    if delete_resp.status_code != 200:
        print(f'Warning: не удалось удалить объект {obj_id}')


@pytest.mark.medium
def test_get_by_id(post_and_delete):
    get_by_id_url = f'{base_url}object/{post_and_delete}'
    response = requests.get(get_by_id_url)
    assert response.status_code == 200


@pytest.mark.critical
def test_patch(post_and_delete):
    update_name = random.choice([True, False])
    update_color = random.choice([True, False])
    update_size = random.choice([True, False])

    if not (update_name or update_color or update_size):
        update_name = True

    current_response = requests.get(f'{base_url}object/{post_and_delete}')
    current_object = current_response.json()
    body = {}

    if update_name:
        body['name'] = fake.name()

    if update_color or update_size:
        new_data = current_object.get('data', {}).copy()
        if update_color:
            new_data['color'] = fake.color_name()
        if update_size:
            new_data['size'] = random.choice(size)
        body['data'] = new_data

    patch_url = f'{base_url}object/{post_and_delete}'
    response = requests.patch(patch_url, json=body)
    assert response.status_code == 200
    print(f'Частично обновили на: {response.text}')


def test_put(post_and_delete):
    update_body = {
        'name': fake.name(),
        'data': {
            'color': fake.color_name(),
            'size': random.choice(size)
        }
    }

    put_url = f'{base_url}object/{post_and_delete}'
    response = requests.put(put_url, json=update_body)
    assert response.status_code == 200
    print(f'Обновили на: {response.text}')
