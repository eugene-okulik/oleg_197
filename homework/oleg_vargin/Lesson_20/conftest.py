import pytest

from api_helpers import post, delete


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
    post_id = None
    try:
        post_id = post()
        yield post_id
    finally:
        if post_id:
            delete(post_id)
