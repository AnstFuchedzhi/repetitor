def sort_words_by_length(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i

        for j in range(i+1, n):
            if len(arr[min_ind]) > len(arr[j]):
                arr[min_ind], arr[j] = arr[j], arr[min_ind]
    return arr 






print(sort_words_by_length(["яблоко", "груша", "киви", "банан"]))
# ['киви', 'груша', 'банан', 'яблоко']