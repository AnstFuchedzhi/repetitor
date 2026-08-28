from main import Product

class BookProduct(Product):
    def __init__(self, author, pages, publish, isbn = None):
        super().__init__(author, pages, publish)

        self.author = author
        self.pages = pages
        self.publish = publish
        self.__isbn = isbn

    def get_info(self):
        return f'Автор: {self.author}, Страниц: {self.pages}, Издательство: {self.publish}, ISBN: {self.__isbn}'

    @property
    def book_isbn(self):
        return f'Текущий номер ISBN: {self.__isbn}'

    @book_isbn.setter
    def book_isbn(self, number):
        count = len(str(number))
        if not isinstance(number, int):
            raise ValueError('Ошибка валидации')
        if count > 13 and count < 13:
            raise ValueError('Ошибка валидации')
        self.__isbn = number
        print('Номер ISBN изменен')
        return number

book = BookProduct('Bulgakov', 250, 'ECSMO', 1234567891234)
print(book.get_info())

print(book.book_isbn)
book.book_isbn = 7987654321098
print(book.book_isbn)


    



        