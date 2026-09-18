import itertools

def compress_sequence(sequence):
    # Используем groupby для группировки подряд идущих одинаковых элементов
   return [(key, len(list(group))) for key, group in itertools.groupby(sequence)]

original = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1]
compressed = compress_sequence(original)
print(compressed)  # [(1, 3), (2, 2), (3, 4), (1, 2)]