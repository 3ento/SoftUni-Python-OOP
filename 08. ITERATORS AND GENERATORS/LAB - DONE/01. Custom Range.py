class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            self.start += 1
            return self.start - 1
        else:
            raise StopIteration()


a = custom_range(1, 10)
for num in a:
    print(num)