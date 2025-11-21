def possible_permutations(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for idx in range(len(lst)):
            for perm in possible_permutations(lst[:idx] + lst[idx + 1:]):
                yield [lst[idx]] + perm

# import itertools
#
# def possible_permutations(lst):
#     for perm in itertools.permutations(lst):
#         yield list(perm)



[print(n) for n in possible_permutations([1, 2, 3])]
print()
[print(n) for n in possible_permutations([1])]