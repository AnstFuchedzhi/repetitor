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
    def get_total_books(cls):
        """Возвращает общее количество книг."""  
        return cls.total_books

    
    @classmethod
    def from_dict(cls, data):
        """Собирает книгу из словаря."""
        return cls(
            title = data.get('title'),
            author = data.get('author'),
            years = data.get('years'),
            pages = data.get('pages')
        )

    
    @classmethod
    def from_csv(cls, csv_string):
        """Собирает книгу из строки"""
        if not csv_string:
            return f'Строка пустая'
        csv_file = StringIO(csv_string)
        reader = csv.reader(csv_file)
        lst = next(reader)
        return cls (
            title = lst[0],
            author = lst[1],
            years = int(lst[2]),
            pages = int(lst[3])
            )

        
    @staticmethod
    def is_valid_title(title):
        """Проверяет длину названия"""
        count = len(title)
        return True if count > 2 else False

        
    
    @staticmethod
    def is_valid_years(years):
        """Проверяет диапазон года издания"""
        if int(years) < 1000 or int(years) > 2024:
            return False
        return True

    
    @staticmethod
    def formal_title(title):
        """Возвращает заголовок с большой буквы"""
        return title.title()

    def get_info(self):
        """Возвращает информацию о книге"""
        return f'Название: {self.title}, Автор: {self.author}, Год: {self.years}, Кол-во страниц {self.pages}'

    
    def is_long(self):
        """Проверяет длину книги"""
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