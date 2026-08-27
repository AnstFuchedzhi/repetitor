from main import Product

class ElectronicProduct(Product):
    def __init__(self, name, price, stock, brand, garanty ):
        super().__init__(name, price, stock)

        self.brand = brand
        self.garanty = garanty

    def get_info(self):
        return f'Товар: {self.name}, Цена: {self._price}, Бренд: {self.brand}, Гарантия: {self.garanty}'



product = ElectronicProduct('pencil', 23000, 15, 'ZaraHome', 1)
print(product.get_info())