class BaseAsserts:
    @staticmethod
    def assert_fields(obj, **expected_fields):
        for field, expected_value in expected_fields.items():
            actual_value = obj.get(field)
            assert actual_value == expected_value, \
                f'Поле {field}: ожидалось {expected_value}, получено {actual_value}'

    @staticmethod
    def assert_status_code(response, expected_status=200):
        assert response.status_code == expected_status, f'Ожидался статус {expected_status}, получен: {response.status_code}'

    @staticmethod
    def assert_update(response, expected_name=None, expected_data=None):
        if expected_name is not None:
            assert response['name'] == expected_name, f'Имя: {response["name"]} != {expected_name}'
        if expected_data is not None:
            assert response['data'] == expected_data, f'Данные: {response["data"]} != {expected_data}'