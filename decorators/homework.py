def uppercase_result(func):
    def wrapper(word):
        if isinstance(word, str):
            result = word.upper()
            return func(result)
        return None
    return wrapper

@uppercase_result
def get_greeting(word):
    return f"привет, {word}!"

print(get_greeting('Анна'))

#я не знаю как перевести в верхний регистр еще и слово привет(







