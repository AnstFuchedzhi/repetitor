def sorted(arr): #по убыванию
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr




print(sorted([5, 2, 8, 1, 9, 3]))