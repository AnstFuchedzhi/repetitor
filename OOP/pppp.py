class Product:
    discount_rate = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def discount(cls, percent):
        cls.discount_rate = percent
    @classmethod
    def get_discount_rate(cls):
        return cls.discount_rate

Product.discount(10)
print(Product.get_discount_rate())
        