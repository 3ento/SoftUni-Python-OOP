def fibonacci():
    f1 = 0
    f2 = 1
    yield f1
    yield f2

    fn1 = f2
    fn2 = f1

    while True:
        fn = fn1 + fn2
        yield fn
        fn2 = fn1
        fn1 = fn


generator = fibonacci()
for i in range(5):
    print(next(generator))