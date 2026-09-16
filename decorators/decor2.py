from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Функция"""
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper 
    return decorator    


@repeat(3)
def say_hello(name):
    """Функция say_hello"""
    print(f'hello{name}')

say_hello('ZZZ')

print(say_hello.__name__)
print(say_hello.__doc__)
