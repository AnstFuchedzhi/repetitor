from main import Product
from main import Category

class BookProduct(Product):
    def __init__(self, name, price, stock, author, pages, publish, isbn = None, category = None, discount = None):
        super().__init__(name, price, stock, category, discount)

        self.author = author
        self.pages = pages
        self.publish = publish
        self.__isbn = isbn

    def get_info(self):
        return f'Автор: {self.author}, Страниц: {self.pages}, Издательство: {self.publish}, ISBN: {self.__isbn}, Категория: {category.name}'

    @property
    def book_isbn(self):
        return f'Текущий номер ISBN: {self.__isbn}'

    @book_isbn.setter
    def book_isbn(self, number):
        clean_number = str(number).replace('-', '')
        count = len(str(clean_number))
        if not clean_number.isdigit():
            raise ValueError('Ошибка валидации')
        if count != 13:
            raise ValueError('Ошибка валидации')
        self.__isbn = clean_number
        print('Номер ISBN изменен')
        return clean_number


category = Category('books', 'very interesting book')
book = BookProduct(
    name= 'Мастер и Маргарита',
    price= 2000,
    stock= 20,
    author= 'Булгаков',
    pages= 250,
    publish= 'ЭКСМО',
    isbn= '123-45-678-91-234',
    category= category,
    discount= 0
)

print(book.price_s)
print(book.get_info())
print(book.book_isbn)
book.book_isbn = '987-654-321-9876'
print(book.book_isbn)

print(category.discription)



    



        