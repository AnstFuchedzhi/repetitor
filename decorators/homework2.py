
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f'Ошибка: {e}'
    return wrapper



@handle_error
def divide(a, b):
    return a / b

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # Ошибка: division by zero


