
def count_calls(func):
    count = 0

    def counter_inner(*args, **kwargs):
        nonlocal count
        count += 1
        return func(*args, **kwargs)
    def get_count():
        return count
    counter_inner.get_count = get_count
    return counter_inner


@count_calls
def greeting(n):
    return f'hello {n}'



print(greeting('S'))
print(greeting('S'))
print(greeting('S'))
print(greeting('S'))
print(greeting('S'))
print(greeting.get_count())


