def operation_decorator(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            new_operation = '*'
        elif first == second:
            new_operation = '+'
        elif first > second:
            new_operation = '-'
        elif first < second:
            new_operation = '/'
        else:
            new_operation = operation
        return func(first, second, new_operation)
    return wrapper


first, second = int(input('Enter first number: ')), int(input('Enter second number: '))


@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second == 0:
            return "Ошибка: деление на ноль!"
        return first / second
    else:
        return "Неизвестная операция"


result = calc(first, second, '+')  # можно передать любую операцию
print("Результат:", result)
