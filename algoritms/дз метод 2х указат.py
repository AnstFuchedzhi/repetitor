def two_diff(arr, target):
    left = 0
    right = 1

    while right < len(arr):
        current_diff = arr[right] - arr[left]
        if current_diff == target:
            return (arr[right], arr[left])
        elif current_diff > target:
            left += 1
        else:
            right += 1

    return None

arr = [0, 2 , 4, 6, 7, 14]
print(two_diff(arr, 3))

        