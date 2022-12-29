class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.count * self.step:
            raise StopIteration

        temp = self.start
        self.start += self.step
        return temp


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

# 100/100
