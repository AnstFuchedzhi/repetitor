def selection(arr):
    n = len(arr)
    for i in range(0, n):
        minim_1 = i
        for j in range(i + 1, n):
            if arr[minim_1] > arr[j]:
                minim_1 = j
        arr[i],arr[minim_1] = arr[minim_1], arr[i]
    return arr

print(selection([5, 2, 4, 7, 1, 9]))
