
def binary_search_last(massiv, number):
    left = 0
    right = len(massiv) - 1
    result = -1
    while left <= right:
        mid = (left + right)// 2
        if number == massiv[mid]:
            result = mid
            left = mid + 1
        elif number > massiv[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return result
        
        



print(binary_search_last([1, 2, 2, 2, 3, 4, 5], 2))   # 3
print(binary_search_last([1, 2, 2, 2, 3, 4, 5], 3))   # 4
print(binary_search_last([1, 2, 2, 2, 3, 4, 5], 6))   # -1
print(binary_search_last([5, 5, 5, 5, 5], 5))         # 4
print(binary_search_last([1, 3, 5, 7, 9], 5))         # 2