def assert_fields(obj, **expected_fields):
    for field, expected_value in expected_fields.items():
        actual_value = obj.get(field)
        assert actual_value == expected_value, \
            f'Поле {field}: ожидалось {expected_value}, получено {actual_value}'
