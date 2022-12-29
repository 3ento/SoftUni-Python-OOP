def type_check(type1):
    def decorator(ref_func):
        def wrapper(*args):
            if isinstance(*args, type1):
                return ref_func(*args)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

# 100/100
