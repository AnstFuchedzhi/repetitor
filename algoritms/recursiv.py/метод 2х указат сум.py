def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[right], arr[left])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

arr = [0, 3, 4, 6, 8, 10, 13]
print(two_sum(arr, 14))
