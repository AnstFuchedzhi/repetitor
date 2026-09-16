def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_result
def get_greeting(word):
    return f"привет, {word}!"

print(get_greeting('Анна'))









