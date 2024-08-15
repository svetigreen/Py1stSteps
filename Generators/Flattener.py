def flatten(nested_list):
    for sublist in nested_list:
        for element in sublist:
            yield element


def flatten_deeply(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_deeply(element)
        else:
            yield element


nested = [[6, 2], [3, 4], [5]]
n_sorted = sorted(flatten(nested))
print(n_sorted)

nested_deeply = [[6, 2, [10, 11]], [3, 4], [[9, 8], 5]]
flattened_list = sorted(flatten_deeply(nested_deeply))
print(flattened_list)


