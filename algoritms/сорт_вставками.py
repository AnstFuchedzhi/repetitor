def sort_insertion(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        last = i - 1
        while last >= 0 and arr[last] > current:
            arr[last + 1] = arr[last]
            last -= 1
        arr[last + 1] = current
    return arr

print(sort_insertion([5, 2, 8, 1, 9, 3]))



