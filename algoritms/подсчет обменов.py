def sorted(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        swapped = False

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                count += 1

        if not swapped:
            break
        
    return arr, count




print(sorted([5, 2, 8, 1, 9, 3]))