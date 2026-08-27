class Animal:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def get_info(self):
        return f' {self.age}, {self.name}'

    def eat(self):
        return f'Животное {self.name} ест'

    def sleep(self):
        return f'Животное {self.name} спит'


class Dog(Animal):

    def __init__(self, age, name, breed):
        super().__init__(age, name)
        self.breed = breed

    def sound(self):
        return f'Животное {self.name} издает звук гав'

    def get_info(self):
            return f' {self.age} {self.name} {self.breed}'


class Cat(Animal):
    def sound(self):
        return f'Животное {self.name} издает звук мяу'


dog = Dog(3, 'H', 'pekines')
print(dog.get_info())
    