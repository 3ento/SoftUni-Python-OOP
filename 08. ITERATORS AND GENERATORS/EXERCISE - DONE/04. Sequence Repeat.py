class sequence_repeat:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.num:
            temp = self.start
            self.start += 1
            return self.seq[temp % len(self.seq)]
        else:
            raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

# 100/100
