def read_next(*args):
    for i in args:
        if isinstance(i, tuple) or isinstance(i, list):
            for el in i:
                yield str(el)
        elif isinstance(i, str):
            yield i
        elif isinstance(i, dict):
            for keys, value in i.items():
                yield keys


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')

# 100/100
