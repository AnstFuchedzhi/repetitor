#Задание 1.1

def func1(arr):
    return arr[0]     #O(1)
#Задание 1.2

def func2(arr):
    total = 0
    for x in arr:
        total += x
    return total      #O(n) линейная сложность
#Задание 1.3

def func3(arr):
    for i in arr:
        for j in arr:
            print(i, j)   #O(n**2) квадратичная сложность
#Задание 1.4

def func4(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:    #O(n**2)
                return True
    return False
#Задание 1.5

def func5(n):
    i = 1
    while i < n:
        print(i)
        i *= 2       #O(log n)
#Задание 1.6

def func6(arr):
    for x in arr:
        print(x)
    for y in arr:
        print(y)    #O(n**2)
#Задание 1.7

def func7(arr):
    n = len(arr)
    for i in range(n):
        for j in range(100):
            print(arr[i], j)   #O(n)
#Задание 1.8

def func8(n):
    for i in range(n):
        j = 1            #O(log n)
        while j < n:
            j *= 2
            print(i, j)
#Задание 1.9

def func9(arr):
    return sorted(arr)     #O(n)
#Задание 1.10

def func10(n):
    if n <= 1:           
        return n
    return func10(n - 1) + func10(n - 2)     #O(n**2)
