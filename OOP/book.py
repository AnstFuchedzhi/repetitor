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


    """Возвращает общее количество книг."""
    @classmethod
    def get_total_books(cls):  
        return cls.total_books

    """Собирает книгу из словаря."""
    @classmethod
    def from_dict(cls, data):
        return cls(
            title = data.get('title'),
            author = data.get('author'),
            years = data.get('years'),
            pages = data.get('pages')
        )

    """Собирает книгу из строки"""
    @classmethod
    def from_csv(cls, csv_string):
        if not csv_string:
            return f'Строка пустая'
        csv_file = StringIO(csv_string)
        reader = csv.reader(csv_file)
        lst = next(reader)
        return cls (
            title = lst[0],
            author = lst[1],
            years = lst[2],
            pages = lst[3]
            )

    """Проверяет длину названия"""    
    @staticmethod
    def is_valid_title(title):
        count = len(title)
        return True if count > 2 else False

        
    """Проверяет диапазон года издания"""
    @staticmethod
    def is_valid_years(years):
        if years < 1000 or years > 2024:
            return True
        return False

    """Возвращает заголовок с большой буквы"""
    @staticmethod
    def formal_title(title):
        my_title = title
        return my_title.title()

    """Возвращает информацию о книге"""
    def get_info(self):
        return f'Название: {self.title}, Автор: {self.author}, Год: {self.years}, Кол-во страниц {self.pages}'

    """Проверяет длину книги"""
    def is_long(self):
        return True if self.pages > 500 else False


book1 = Book('коллекционер', 'Фаулз', 2017, 250)
print(book1.get_info())

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
print(Book.is_long(book1))
print(Book.get_total_books())