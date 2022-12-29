def possible_permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in possible_permutations(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


for n in possible_permutations([1, 2, 3]):
    print(n)

# 50/50
