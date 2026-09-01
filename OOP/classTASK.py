import datetime

class Task:

    task_counter = 0          #счётчик для генерации ID задач
    total_tasks = 0           #общее количество созданных задач
    completed_tasks = 0        #количество выполненных задач
    priority_levels = {}       #словарь с названиями приоритетов (должен быть: {1: "Низкий", 2: "Средний", 3: "Высокий"})
    priority_emojis = {}       #словарь с эмодзи приоритетов (должен быть: {1: "🟢", 2: "🟡", 3: "🔴"})
    

    def __init__(self, id, title, description, priopity, is_done, create_at, due_date = None, tags=[], history = []):
        self.id = id
        self.title = title
        self.description = description
        self.priopity = priopity
        self.is_done = is_done
        self.create_at = datetime.now()
        self.due_date = due_date
        self.tags = []
        self.__history = []

    
    def mark_done(self):
        self.completed_tasks += 1
        self.__history.append(self.completed_tasks)
        return f'Одна задача выполнена'

    def mark_undone(self):
        self.completed_tasks -= 1
        self.__history.remove(self.completed_tasks)
        return 'Выполнение задачи отменено'

    def get_priority_name(self, data):
        return data[]


    

task1 = Task(1, 'Задача 1', 'Отправить письмо', '🟢', )

data = {1: "🟢", 2: "🟡", 3: "🔴"}
