def binar(arr, number, left=0, right = None):
    if right == None:
        right = len(arr) - 1
    mid = (left + right)// 2
    if number == arr[mid]:
        return mid
    elif number < arr[mid]:
        return binar(arr, number, left, right = mid - 1)
    elif number > arr[mid]:
        return binar(arr, number, mid + 1, right)


print(binar([1, 3, 4, 7, 6, 8], 3))
    
