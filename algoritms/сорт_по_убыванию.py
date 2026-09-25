def selection(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i

        for j in range(i + 1, n):
            if arr[min_ind]< arr[j]:
                arr[min_ind], arr[j] = arr[j], arr[min_ind]

    return arr

arr = [5, 2, 6, 8, 3, 1]
print(selection(arr))