def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        last = i - 1
        while last >=0 and arr[last] < current:
            arr[last + 1] = arr[last]
            last -= 1
        arr[last + 1] = current
    return arr    








print(insertion_sort_desc([5, 2, 8, 1, 9, 3]))  # [9, 8, 5, 3, 2, 1]
print(insertion_sort_desc([1, 2, 3]))            # [3, 2, 1]
print(insertion_sort_desc([7]))                  # [7]