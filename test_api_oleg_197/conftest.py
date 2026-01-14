import pytest

from endpoints.create_post import CreatePost
from endpoints.delete_post import DeletePost


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
    create = CreatePost()
    delete = DeletePost()
    post_id = None
    try:
        post_id = create.create()
        yield post_id
    finally:
        if post_id:
            delete.delete(post_id)
