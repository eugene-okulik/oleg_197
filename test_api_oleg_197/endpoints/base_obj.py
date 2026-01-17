from abc import ABC, abstractmethod


class BaseObj(ABC):
    @abstractmethod
    def _make_request(self, post_id, name=None, data=None):
        pass

    def assert_update(self, post_id, name=None, data=None, expected_name=None, expected_data=None):
        response = self._make_request(post_id, name, data)

        if expected_name is not None:
            assert response['name'] == expected_name, f'Имя: {response["name"]} != {expected_name}'
        if expected_data is not None:
            assert response['data'] == expected_data, f'Данные: {response["data"]} != {expected_data}'

        return response
