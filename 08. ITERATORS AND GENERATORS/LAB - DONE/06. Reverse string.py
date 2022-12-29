def reverse_text(string):
    num = 1
    while num <= len(string):
        yield string[-num]
        num += 1


for char in reverse_text("Python"):
    print(char, end='')