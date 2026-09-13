
def count_calls(func):
    def inner(*args, **kwargs):
        inner.count += 1
        return func(*args, **kwargs)
    inner.count = 0
    return inner

@count_calls
def some_func():
    return f'Вызов функции'

some_func()
some_func()
some_func()

print(some_func.count)
