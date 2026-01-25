import pytest

from test_api_oleg_197.endpoints.create_obj import CreateObj
from test_api_oleg_197.endpoints.delete_obj import DeleteObj
from test_api_oleg_197.endpoints.get_obj import GetObj
from test_api_oleg_197.endpoints.put_obj import PutObj
from test_api_oleg_197.endpoints.patch_obj import PatchObj


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
    create = CreateObj()
    delete = DeleteObj()
    post_id = None
    try:
        post_id = create.create()
        yield post_id
    finally:
        if post_id:
            delete.delete(post_id)


@pytest.fixture
def creator():
    return CreateObj()


@pytest.fixture
def deleter():
    return DeleteObj()


@pytest.fixture
def getter():
    return GetObj()


@pytest.fixture
def putter():
    return PutObj()


@pytest.fixture
def patcher():
    return PatchObj()


@pytest.fixture()
def created_obj():
    creator = CreateObj()
    post_id = creator.create()
    yield post_id
