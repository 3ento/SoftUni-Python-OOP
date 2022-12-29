class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "y", "Y"]
        self.start = 0
        self.txt_vow = [el for el in self.string if el in self.vowels]
        self.end = len(self.txt_vow) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        index = self.start
        self.start += 1
        return self.txt_vow[index]



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)