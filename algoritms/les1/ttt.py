def insertion_sort(arr):
    result = []
    for i in arr:
        position = 0
        while position < len(result) and result[position] < i:
            position += 1
        result.insert(position, i)
    return result

print(insertion_sort([5, 2, 8, 1, 9, 3]))