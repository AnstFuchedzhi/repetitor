import csv
from io import StringIO

class Book:
    total_books = 0

    def __init__(self, title, author, years, pages):
        self.title = title
        self.author = author
        self.years = years
        self.pages = pages
        Book.total_books += 1

    @classmethod
    def get_total_books(cls):  #возвращает общее кол-во книг
        return cls.total_books

    @classmethod
    def from_dict(cls, data):
        return cls(
            title = data.get('title'),
            author = data.get('author'),
            years = data.get('years'),
            pages = data.get('pages')
        )

    @classmethod
    def from_csv(cls, csv_string):
        csv_file = StringIO(csv_string)
        reader = csv.reader(csv_file)
        lst = next(reader)
        return cls (
            title = lst[0],
            author = lst[1],
            years = lst[2],
            pages = lst[3]
        )
        
    @staticmethod
    def is_valid_title(title):
        count = len(title)
        if not title:
            return f'Пусто'
        if count > 2:
            return f'Название больше 2х символов'
        return f'Название содержит не больше 2х символов'

    @staticmethod
    def is_valid_years(years):
        if years < 1000 or years > 2024:
            return f'Дата выпуска книги не в диапазоне от 1000г до 2024г'
        return f'Книга в нужном диапазоне'

    @staticmethod
    def formal_title(title):
        my_title = str(title)
        return my_title.title()


    def get_info(self):
        return f'Название: {self.title}, Автор: {self.author}, Год: {self.years}, Кол-во страниц {self.pages}'

    def is_long(self):
        return True if self.pages > 500 else False


book1 = Book('коллекционер', 'Фаулз', 2017, 250)
print(book1.get_info())
print(book1.is_long())
data = {
    'title' : 'Война и Мир',
    'author': 'Толстой',
    'years' : 1869,
    'pages' : 560
}
book2 = Book.from_dict(data)
print(Book.get_info(book2))

csv_str = 'Мастер и Маргарита, Булгаков, 1940, 240'
book3 = Book.from_csv(csv_str)
print(Book.get_info(book3))
print(Book.is_valid_title(book2.title))
print(Book.is_valid_years(book1.years))
print(Book.formal_title(book1.title))

print(Book.get_total_books())