a = float(input('Введите число: '))
b = float(input('Введите число: '))
c = float(input('Введите число: '))

result_1 = a + b + c
result_2 = (a + b + c)/ 3
result_3 = (a * b)
round_number = round(result_3, 2)


print(f'{result_1:.2f}')
print(f'{result_2:.2f}')
print(f'{result_3:.2f}')
