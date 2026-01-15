import allure
import random
import requests
import faker
import pytest

from test_api_oleg_197.endpoints.endpoints import Endpoints
from test_api_oleg_197.endpoints.create_obj import CreateObj
from test_api_oleg_197.endpoints.delete_obj import DeleteObj
from test_api_oleg_197.endpoints.get_obj import GetObj
from test_api_oleg_197.endpoints.put_obj import PutObj
from test_api_oleg_197.endpoints.patch_obj import PatchObj

fake = faker.Faker()
size = ['XS', 'S', 'M', 'L', 'XL', 'AVERAGE', 'UNBELIEVABLE']


@allure.title('Создание объекта: {name}')
@pytest.mark.critical
@pytest.mark.parametrize('name', ['test_1', 'test_2', 'test_3'])
def test_post(name, creator, deleter, getter):
    post_id = creator.create_with_name(name=name)

    obj = getter.get(post_id)
    assert obj['name'] == name

    deleter.delete(post_id)


@allure.title("Получение объекта по ID")
@pytest.mark.medium
def test_get_by_id(post_and_delete, getter):
    obj = getter.get(post_and_delete)
    assert obj['id'] == post_and_delete


@allure.title('Частичное обновление объекта (PATCH)')
@pytest.mark.critical
def test_patch(post_and_delete, patcher, getter):
    original = getter.get(post_and_delete)

    update_name = random.choice([True, False])
    update_color = random.choice([True, False])
    update_size = random.choice([True, False])

    if not (update_name or update_color or update_size):
        update_name = True

    new_name = fake.name() if update_name else None
    new_data = None

    if update_color or update_size:
        current_data = original.get('data', {})
        new_data = current_data.copy()
        if update_color:
            new_data['color'] = fake.color_name()
        if update_size:
            new_data['size'] = random.choice(size)

    updated = patcher.patch(post_and_delete, name=new_name, data=new_data)

    if new_name:
        assert updated['name'] == new_name
    if new_data:
        assert updated['data'] == new_data


@allure.title('Полное обновление объекта (PUT)')
@pytest.mark.medium
def test_put(post_and_delete, putter):
    new_name = fake.name()
    new_data = {
        'color': fake.color_name(),
        'size': random.choice(size)
    }

    updated = putter.put(post_and_delete, name=new_name, data=new_data)

    assert updated['name'] == new_name
    assert updated['data'] == new_data


@allure.title("Проверка удаления объекта")
@pytest.mark.medium
def test_check_delete(created_obj, deleter, getter):
    post_id = created_obj
    deleter.delete(post_id)
    getter.assert_deleted(post_id)
