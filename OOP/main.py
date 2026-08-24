class Product:

    def __init__(self, name, price, stock, category = None ):

        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def get_info(self):
        category_name = self.category.name if self.category else 'без категории'
        return f'Товар: {self.name}, Цена: {self.price}, Категории {category_name}'

    def reduce_stock(self, count=1):
        if count > self.stock:
            return f'Не можем выдать столько. На складе {self.stock} товаров'
        self.stock -= count

    def increase(self, count=1):
        self.stock += count



class Category:

    def __init__(self, name, discription=''):
        self.name = name
        self.discription = discription
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)
        return f'Товар {product.name} добавлен в катеригорию {self.name}'

    def get_products(self):
        return self.__products

    def info(self):
        return f'Название категории {self.name}, Описание: {self.discription}, Кол-во товаров: {len(self.__products)}'

elecrtonic = Category('Электроника', 'Все виды электроники')
laptop = Product('Ноутбук', 63000, 10, elecrtonic)
print(laptop.get_info())
    