import datetime
import csv
from io import StringIO
from datetime import time
from datetime import timedelta

class Task:

    task_counter = 0          #счётчик для генерации ID задач
    total_tasks = 0           #общее количество созданных задач
    completed_tasks = 0        #количество выполненных задач
    priority_levels = {1: "Низкий", 2: "Средний", 3: "Высокий"}     
    priority_emojis = {1: "🟢", 2: "🟡", 3: "🔴"}  
    

    def __init__(self, id, title, description, priority, is_done=False, due_date = None, tag=[], history = []):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.is_done = is_done
        self.create_at = datetime.datetime.now()
        self.due_date = due_date
        self.tag = tag
        self.__history = []
        Task.total_tasks += 1
        

    
    def mark_done(self):
        if not self.is_done:
            self.is_done = True
            Task.completed_tasks += 1
            self.__history.append(self.completed_tasks)
            return f'Одна задача выполнена'
        return f'Задача уже выполнена'

    def mark_undone(self):
        self.completed_tasks -= 1
        self.__history.remove(self.completed_tasks)
        return 'Выполнение задачи отменено'

    def get_priority_name(self):
        return self.priority_levels.get(self.priority, 'Нет приоритета')
           
    def get_priority_emoji(self):
        return self.priority_emojis.get(self.priority, 'Нет приоритета')

    def add_tag(self, tag):
        if not tag:
            return f'Внесите тег, строка пустая' 
        if tag in self.tag:
            return f'Тег {tag} уже есть'
        else:
            self.tag.append(tag)
            return f'Тег {tag} добавлен'


    def remove_tag(self, tag):
        if not tag:
            return f'Введите тег, строка пустая'
        if tag in self.tag:
            self.tag.remove(tag)
            return f'Тег {tag} удален'


    def is_overdue(self):
        if not self.due_date:
            return False
        else:
            return datetime.datetime.now() > self.due_date and not self.is_done
            
    def days_until_due(self):
        if not self.due_date:
            return None
        count_days = datetime.datetime.now() - self.due_date
        return count_days


    def get_history(self):
        self.__history.append(self.description)
        return self.__history


    def get_info(self):
        due_date_str = self.due_date.strftime("%Y-%m-%d %H:%M:%S") if self.due_date else None
        return f'{self.id}, {self.title}, {self.description}, {self.is_done}, {due_date_str}, {self.tag}'

    def __repr__(self):
            return f'ID:{self.id}, Название:{self.title}, Описание:{self.description}, Приоритет: {self.get_priority_emoji()}, {self.get_priority_name()}'

    def __str__(self):
        return f'ID:{self.id}, Название:{self.title}, Описание:{self.description}, Приоритет: {self.get_priority_emoji()}, {self.get_priority_name()}'

    @classmethod
    def get_total_tasks(cls):
        return cls.total_tasks

    @classmethod
    def get_completed_tasks(cls):
        return cls.completed_tasks

    @classmethod
    def get_pending_tasks(cls):
        return cls.total_tasks - cls.completed_tasks

    @classmethod
    def get_completion_rate(cls):  #возвращает процент выполнения (completed / total * 100)
        return cls.completed_tasks/ cls.total_tasks * 100

    @classmethod
    def from_dict(cls, data):    #создаёт задачу из словаря (ключи: title, description, priority, due_date, tags)
        tag = data.get('tag')      #не поняла почему именно так получаем, а не со всеми в return
        due_date = data.get('due_date')
        if isinstance(due_date, timedelta): #не поняла почему именно так получаем, а не со всеми в return
            due_date = datetime.datetime.now() + due_date

        return cls(
            id = data.get('id'),
            title = data.get('title'),
            description = data.get('description'),
            priority = int(data.get('priority')),
            due_date = due_date,
            tag = tag                    
        )
        
    @classmethod
    def from_csv(cls, csv_string): #создаёт задачу из CSV-строки (формат: "title,description,priority,due_date,tags"
        if not csv_string:
            return f'Пустая строка'
        csv_file = StringIO(csv_string)
        reader = csv.reader(csv_file)
        lst = next(reader)
        return cls(
            id = lst[0],
            title = lst[1],
            description = lst[2],
            priority = int(lst[3]),
            due_date = lst[4], #эти два не работают, в интернете написано нужно как то их преобразовать, но я не понимаю как и для чего, и откуда сюда достается due_date tegs
            tag = lst[5]
        ) 





task1 = Task(1111, 'Задача 1', 'Отправить письмо', 1, False,  datetime.datetime.now() - timedelta(days=2))
task2 = Task(2222, 'Задача 2', 'Сходить в магазин', 2, True)
csv_str = '4444, Задача 4, Полить цветы, 1, timedelta(hours=12), домашние дела'
print(task1.get_priority_name())
print(task1.get_priority_emoji())
print(task1.mark_done())
print(task2.mark_done())
print(task1.add_tag('важное'))
print(task1.is_overdue())
print(task1.days_until_due())
print(task1.get_history())
print(task1.get_info())
print(task1)
print(task2)
print(Task.total_tasks)
print(Task.completed_tasks)
print(Task.get_pending_tasks())
print(Task.get_completion_rate())
data = {
    'id' : '33333',
    'title' : 'Задча 3',
    'description' : 'Погулять с собакой',
    'priority' : 3,
    'due_date' : timedelta(hours=8),
    'tag' : 'домашние дела'
}

task3 = Task.from_dict(data)
print(task3.get_info())
task4 = Task.from_csv(csv_str)
print(task4)