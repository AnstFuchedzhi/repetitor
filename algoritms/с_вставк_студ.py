students = [
    {"name": "Анна", "age": 25},
    {"name": "Иван", "age": 22},
    {"name": "Мария", "age": 23},
    {"name": "Пётр", "age": 21},
]

def sort_students_by_age(students):
    n = len(students)
    for i in range(1, n):
        current = students[i]
        last = i - 1
        while last >= 0 and students[last]['age'] > current['age']:
            students[last + 1] = students[last]
            last -= 1
        students[last + 1] = current
    return students


sorted_students = sort_students_by_age(students)
for s in sorted_students:
    print(f"{s['name']}: {s['age']}")



# Пётр: 21
# Иван: 22
# Мария: 23
# Анна: 25