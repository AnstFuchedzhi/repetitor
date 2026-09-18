def average_score(students, student_name):
    marks_student = students.get(student_name)
    count = len(marks_student)
    midle = sum(marks_student)/count
    round_midle = round(midle, 2)
    return round_midle

        
   

students = {'Ivan': [41, 52, 74], 'Olga': [88, 90, 91]}
student_name = 'Ivan'

print(average_score(students, student_name))

