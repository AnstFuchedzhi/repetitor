def even_numbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            yield i
            i -= 1

for num in even_numbers(10):
    print(num)