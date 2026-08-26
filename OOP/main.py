import datetime
from datetime import datetime

class Product:

    def __init__(self, name, price, stock, category = None, discount = 0 ):

        self.name= name
        self.price = price
        self.__stock = stock
        self.category = category
        self.__discount = discount

    @property
    def product_discount(self):
        return self.__discount

    @product_discount.setter
    def product_discount(self, value):
        if not isinstance(value, int):
            raise ValueError('Ошибка валидации')
        if value > 0 and value < 100:
            self.__discount = value
            print(f'Размер скидки успешно заменен на {value}')

    @property
    def stock(self): #возвращает кол-во товаров на складе
        return self.__stock


    @stock.setter
    def stock(self, value):
        if not isinstance(value, int):
            raise ValueError('Ошибка Валидации')
        if value < 0:
            raise ValueError('Ошибка Валидации')
        self.__stock = value
        print(f'Кол-во товара {self.name} на складе успешно заменено на {value}')
        

    @property
    def price_s(self):
        return f'Цена на товар {self.name} - {self.price}'
    

    @price_s.setter
    def price_s(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Ошибка Валидации')
        if value < 0:
            raise ValueError('Ошибка Валидации')
        self.price = value
        print(f'Цена на товар {self.name} успешно заменено на {value}')


    def get_info(self):
        category_name = self.category.name if self.category else 'без категории'
        return f'Товар: {self.name}, Цена: {self.price}, Категории {category_name}'

    def reduce_stock(self, count=1):
        if count > self.__stock:
            return f'Не можем выдать столько. На складе {self.__stock} товаров'
        self.stock_s -= count

    @property
    def is_in_stoke(self):
        if self.__stock > 0:
            return True
        return False

    def increase(self, count=1):
        self.stock_s += count

    def apply_discount(self, percent): #уменьшает цену на указанный процент
        discount = self.price/percent
        result = self.price - discount
        return f'На товаре: {self.name} скидка {percent}%, теперь цена на товар {result}'

    def remove_discount(self):
        self.__discount = 0
        return f'Скидка с товара {self.name} удалена, теперь цена товара {self.price}'
    
    @property
    def get_total_value(self): #возвращает общую стоимость товаров на складе
        all_count = self.price * self.__stock
        return f'Общая стоимость товаров {self.name} - {all_count}'


    

class Category: #😍😍😍

    def __init__(self, name, discription=''):
        self.name= name
        self.discription = discription
        self.__created_at_time = datetime.now()
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

    @property
    def create(self):
        self.__created_at_time = datetime.now()
        return f'Дата и время создания категории {self.name} - {self.__created_at_time.strftime("%Y-%m-%d %H:%M:%S")}'

    def get_product_count(self):
        count_product = len(self.__products)
        return f'В категории {self.name} всего {count_product} позиции'

    def get_avg_price(self):
        total = 0
        count_len = len(self.__products)
        for product in self.__products:
            if count_len == 0:
                return 0
        total += product.price
        average = total // count_len
        return f'Средняя цена товаров в категории {self.name}: {average}'


elecrtonic = Category('Электроника', 'Все виды электроники')
laptop = Product('Ноутбук', 63000, 10, elecrtonic)
phone = Product('Телефон', 55000, 12, elecrtonic )
microwave = Product('Микроволновка', 7000, 13, elecrtonic)
print(laptop.get_info())
print(laptop.apply_discount(10))
print(laptop.get_total_value)
elecrtonic.add_product(laptop)
elecrtonic.add_product(phone)
elecrtonic.add_product(microwave)
print(elecrtonic.remove_product(phone))
print(elecrtonic.get_total_value)
print(elecrtonic.cheapest())
print(phone.price_s)
phone.price_s = 20000
print(phone.price_s)
print(phone.stock)
laptop.stock_s = 25
print(laptop.stock_s)
print(microwave.product_discount)
microwave.product_discount = 5
print(microwave.product_discount)
print(microwave.remove_discount())
print(laptop.is_in_stoke)

print(elecrtonic.create)
print(elecrtonic.get_product_count())
print(elecrtonic.get_avg_price())
