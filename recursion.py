import bisect


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 10 is:", factorial(10))


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print("Power 3 to 4 is:", power(3, 4))


def search(sequence, number, lower=0, upper=None):
    """binary search"""
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


#seq = [34, 67, 8, 123, 4, 100, 95]
#seq.sort()
#print(seq)
#number = int(input("Enter your number you are looking for: "))
#print(f'Found {number} in the seq at position:', search(seq, number))


# Define a sorted list
sorted_list = [1, 3, 4, 6, 8, 9, 11]

# Element to search for
element = 7

# Find the insertion point using bisect_left
index_left = bisect.bisect_left(sorted_list, element)
print(f'Insertion point for {element} using bisect_left: {index_left}')

# Find the insertion point using bisect_right
index_right = bisect.bisect_right(sorted_list, element)
print(f'Insertion point for {element} using bisect_right: {index_right}')

# Insert the element using insort_left
bisect.insort_left(sorted_list, element)
print(f'List after insertion using insort_left: {sorted_list}')
