import datetime
from datetime import datetime
import copy

class Product:

    def __init__(self, name, price, stock, category = None, discount = 10 ):

        self.name= name
        self._price = price
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
        if self.__discount > 0:
            calculation = (self._price * self.__discount)/ 100
            price_with_discount = self._price - calculation
            return f'Цена на товар {self.name} со скидкой - {price_with_discount}'
        return f'Скидки нет, цена на товар {self.name} - {self._price}'

    @price_s.setter
    def price_s(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Ошибка Валидации')
        if value < 0:
            raise ValueError('Ошибка Валидации')
        self._price = value
        print(f'Цена на товар {self.name} успешно заменено на {value}')


    def __repr__(self):
        category_name = self.category.name if self.category else 'без категории'
        return f'Товар: {self.name}, Цена: {self._price}, Категории {category_name}'

    def reduce_stock(self, count=1):
        if count > self.__stock:
            return f'Не можем выдать столько. На складе {self.__stock} товаров'
        self.stock -= count

    @property
    def is_in_stoke(self):
        if self.__stock > 0:
            return True
        return False

    def increase(self, count=1):
        self.stock += count


    def remove_discount(self):
        self.__discount = 0
        return f'Скидка с товара {self.name} удалена, теперь цена товара {self._price}'
    
    @property
    def get_total_value(self): #возвращает общую стоимость товаров на складе
        all_count = self._price * self.__stock
        return f'Общая стоимость товаров {self.name} - {all_count}'

    def __eq__(self, value):
        return self._price == value._price

    def __lt__(self, value):
        return self._price < value._price

    def __gt__(self, value):
        return self._price > value._price
    

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

    def __str__(self):
        return f'Название категории {self.name}, Описание: {self.discription}, Кол-во товаров: {len(self.__products)}'

    def remove_product(self, product_name):
        for product in self.__products:
            if product == product_name.name:
                self.__products.remove(product_name.name)
            return f'Товар {product_name.name} удален из категории {self.name}'

    def get_total_value(self):  #возвр общую стоимость товаров из категории
        total = 0
        for product in self.__products:
            total += product._price * product.stock
        return f'Общая стоимость товаров категории {self.name} - {total}'
           
    def cheapest(self):  #возвращает самый дешевый товар из категории
        if not self.__products :
            return None
        min_product = self.__products[0]
        for product in self.__products:
            if product._price < min_product._price:
                min_product = product
        return f'Самый дешевый товар из каталога {self.name}: {min_product.name} - стоимостью {min_product._price}'

    @property
    def create(self):
        return f'Дата и время создания категории {self.name} - {self.__created_at_time.strftime("%Y-%m-%d %H:%M:%S")}'

    def get_product_count(self):
        count_product = len(self.__products)
        return f'В категории {self.name} всего {count_product} позиции'

    def get_avg_price(self):
        total = sum(product._price for product in self.__products)
        count = len(self.__products)
        avg = total//count
        return f'Средняя цена товаров в категории {self.name}: {avg}'

class Cart: #😎😎😎
    def __init__(self):
        self.__items = []
        self.__total = 0.0

    def add_items(self, product, quantity=1):
        if product.stock >= quantity:
            product.stock -= quantity
            self.__items.append({'product': product, 'quantity': quantity })
            self.__total += product._price * quantity
            return f'Товар {product.name} добавлен в корзину. Сумма товаров в корзине: {self.__total}'
        return f'Недостаточное количество товара {product.name}'

    def remove_items(self, product_name):
        for item in self.__items:
            product = item['product']
            quantity = item['quantity']
            if product.name == product_name:
                self.__items.remove(item)
                product.stock += quantity
                self.__total -= product._price * quantity
                return f'Товар {product.name} удален из корзины. Сумма товаров на складе: {self.__total}'
        return f'Товар не найден'

    def clear(self):
        for item in self.__items:
            product = item['product']
            quantity = item['quantity']
            product.stock += quantity
            self.__total = 0.0
            self.__items.clear()
            return f'Корзина очищена'
        return f'Ошибка'

    def __str__(self):
        total = float(self.__total)
        return f'Общая сумма товаров корзины: {total}'

    def get_items(self):
        copy_lst = copy.deepcopy(self.__items)
        return copy_lst
    
    def __update_total(self):
        total = 0
        for item in self.__items:
            product = item['product']
            quantity = item['quantity']
            total += product.price * quantity
        self.__total = total
        return total

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, key):
        return self.__items[key]

cart = Cart()
elecrtonic = Category('Электроника', 'Все виды электроники')
laptop = Product('Ноутбук', 63000, 10, elecrtonic)
phone = Product('Телефон', 55000, 12, elecrtonic )
microwave = Product('Микроволновка', 7000, 13, elecrtonic)

print(laptop==phone)
print(microwave < laptop)
print(microwave > laptop)

elecrtonic.add_product(laptop)
elecrtonic.add_product(phone)
elecrtonic.add_product(microwave)
print(elecrtonic.get_total_value())
print(elecrtonic.get_avg_price())


print(cart.add_items(laptop, 1))
print(cart)
print(cart.get_items())
print(elecrtonic)
print(len(cart))
print(cart[0])