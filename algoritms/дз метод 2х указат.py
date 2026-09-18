def two_diff(arr, target):
    left = 0
    right = 1

    while left < right:
        current_diff = arr[right] - arr[left]
        if current_diff == target:
            return (arr[right], arr[left])
        elif current_diff > target:
            left += 1
        else:
            right += 1

    return None

arr = [0, 3, 4, 6, 8, 10, 13]
print(two_diff(arr, 5))

        