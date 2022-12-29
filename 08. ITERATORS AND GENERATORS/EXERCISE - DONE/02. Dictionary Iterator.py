class dictionary_iter:
    def __init__(self, dic):
        self.doubles = list(dic.items())
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.doubles):
            raise StopIteration

        temp = self.current
        self.current += 1
        return self.doubles[temp]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# 100/100
