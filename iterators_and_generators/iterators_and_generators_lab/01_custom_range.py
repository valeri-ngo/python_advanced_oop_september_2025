class custom_range:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.count = -1
        self.current = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.end:
            return self.current
        else:
            raise StopIteration

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)