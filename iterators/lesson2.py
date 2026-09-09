
class SquaresIterator:
    def __init__(self, number):
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.number:
            raise StopIteration
        result = self.current**2
        self.current += 1
        return result

iterator = SquaresIterator(10)
for i in iterator:
    print(i)

# при удалении StopIteration числа уходят в бесконечность. Или так и должно быть?🤓