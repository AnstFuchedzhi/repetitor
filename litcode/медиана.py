def mediana(s):
    n = len(s)
    sorted_s = sorted(s)
    if len(s)% 2 != 0:
        return sorted_s[n // 2]
    else:
        mid_1 = s[n // 2]
        mid_2 = s[n//2] - 1
        return (mid_1 + mid_2)/2



print(mediana([1, 2, 3, 4, 5, 6]))
print(mediana([1, 2, 3, 4, 5, 6, 7]))


