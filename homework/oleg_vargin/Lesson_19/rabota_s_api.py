import random
import requests
import faker

fake = faker.Faker()

base_url = 'http://objapi.course.qa-practice.com/'


def get():
    response = requests.get(base_url)
    print(response.text)


def get_by_id(id: int):
    get_by_id_url = f'{base_url}object/{id}'
    response = requests.get(get_by_id_url)
    return response


def post():
    sizes = ['XS', 'S', 'M', 'L', 'XL', 'AVERAGE', 'UNBELIEVABLE']
    body = {
        'name': fake.name(),
        'data': {
            'color': fake.color_name(),
            'size': random.choice(sizes)
        }
    }
    post_url = base_url + 'object'
    response = requests.post(post_url, json=body)
    print(response.text)


def put(id: int, name: str, data: dict):
    if not isinstance(data, dict):
        raise ValueError("Поле 'data' должно быть словарём.")

    body = {
        'name': name,
        'data': data
    }
    put_url = f'{base_url}object/{id}'
    response = requests.put(put_url, json=body)
    print(response.text)


def patch(id: int, name: str = None, color: str = None, size: str = None):
    if name is None and color is None and size is None:
        print("Для работы метода PATCH нужно указать id и хотя бы один параметр: name, color или size")
        return

    current_response = get_by_id(id)
    current_object = current_response.json()
    body = {}

    if name is not None:
        body['name'] = name

    if color is not None or size is not None:
        new_data = current_object.get('data', {}).copy()
        if color is not None:
            new_data['color'] = color
        if size is not None:
            new_data['size'] = size
        body['data'] = new_data

    patch_url = f"{base_url}object/{id}"
    response = requests.patch(patch_url, json=body)

    print(response.text)


def patch_2(id: int, name: str = None, color: str = None, size: str = None):
    if name is None and color is None and size is None:
        print("Для работы метода PATCH нужно указать id и хотя бы один параметр: name, color или size")
        return

    body = {}

    if name is not None:
        body['name'] = name

    if color is not None or size is not None:
        body['data'] = {}
        if color is not None:
            body['data']['color'] = color
        if size is not None:
            body['data']['size'] = size

    patch_url = f'{base_url}object/{id}'
    response = requests.patch(patch_url, json=body)

    print(response.text)


def delete(id: int):
    delete_url = f'{base_url}object/{id}'
    response = requests.delete(delete_url)
    print(response.text)
