massiv = [1, 2, 3, 5, 8, 9, 12, 15, 20]
def elemen(massiv, number):
    left = 0
    right = len(massiv) - 1
    result = -1
    while left<=right:
        mid = (left + right)// 2
        if number == massiv[mid]:
            return mid
        elif number < massiv[mid]:
            right = mid - 1
        elif number > massiv[mid]:
            left = mid + 1



print(elemen(massiv, 9))

