def repeat_me(count):
    def decorator(func):
        def wrapper(*args):
            for _ in range(count):
                func(*args)
        return wrapper
    return decorator


@repeat_me(count=2)
def example(*args):
    print(*args)


example('print me')
