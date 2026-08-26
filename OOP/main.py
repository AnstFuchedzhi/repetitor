class Product:

    def __init__(self, name, price, stock, category = None ):

        self.name= name
        self.price = price
        self.stock = stock
        self.category = category

    @property
    def price_s(self):
        return self.price

    @price_s.setter
    def price_s(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Ошибка Валидации')
        if value < 0:
            raise ValueError('Ошибка Валидации')
        self.price = value
        return 'Успешно'



    def get_info(self):
        category_name = self.category.name if self.category else 'без категории'
        return f'Товар: {self.name}, Цена: {self.price}, Категории {category_name}'

    def reduce_stock(self, count=1):
        if count > self.stock:
            return f'Не можем выдать столько. На складе {self.stock} товаров'
        self.stock -= count

    def increase(self, count=1):
        self.stock += count

    def apply_discount(self, percent): #уменьшает цену на указанный процент
        discount = self.price/percent
        result = self.price - discount
        return result

    def get_total_value(self): #возвращает общую стоимость товаров на складе
        all_count = self.price * self.stock
        return f'Общая стоимость товара {self.name} - {all_count}'

class Category:

    def __init__(self, name, discription=''):
        self.name= name
        self.discription = discription
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)
        return f'Товар {product.name} добавлен в катеригорию {self.name}'

    def get_products(self): #возвращает товары из списка self.__product
        return self.__products

    def info(self):
        return f'Название категории {self.name}, Описание: {self.discription}, Кол-во товаров: {len(self.__products)}'

    def remove_product(self, product_name):
        for product in self.__products:
            if product == product_name.name:
                self.__products.remove(product_name.name)
            return f'Товар {product_name.name} удален из категории {self.name}'

    def get_total_value(self):  #возвр общую стоимость товаров из категории
        total = 0
        for product in self.__products:
            total += product.price * product.stock
        return f'Общая стоимость товаров категории {self.name} - {total}'
           
    def cheapest(self):  #возвращает самый дешевый товар из категории
        if not self.__products :
            return None
        min_product = self.__products[0]
        for product in self.__products:
            if product.price < min_product.price:
                min_product = product

        return f'Самый дешевый товар из каталога {self.name}: {min_product.name} - стоимостью {min_product.price}'

elecrtonic = Category('Электроника', 'Все виды электроники')
laptop = Product('Ноутбук', 63000, 10, elecrtonic)
phone = Product('Телефон', 55000, 12, elecrtonic )
microwave = Product('Микроволновка', 7000, 13, elecrtonic)
print(laptop.get_info())
print(laptop.apply_discount(10))
print(laptop.get_total_value())
elecrtonic.add_product(laptop)
elecrtonic.add_product(phone)
elecrtonic.add_product(microwave)

print(elecrtonic.remove_product(phone))

print(elecrtonic.get_total_value())
print(elecrtonic.cheapest())

print(phone.price_s)
phone.price_s = 20000
print(phone.price_s)