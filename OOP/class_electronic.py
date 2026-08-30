class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            raise ValueError('Ошибка валидации')
        result = self.amount + other.amount
        return Money(result)

    def __str__(self):
        return f'{self.amount}'

    def __eq__(self, value):
        if not isinstance(value, Money):
            raise ValueError('Ошибка валидации')
        return self.amount == value.amount

    def __lt__(self, value):
        if not isinstance(value, Money):
            raise ValueError('Ошибка валидации')
        return self.amount < value.amount
    

am1 = Money(2000)
am2 = Money(1000)

print(am1 + am2)
print(am1 == am2)
print(am1 > am2)


