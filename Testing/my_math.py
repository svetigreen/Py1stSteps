def square(x):
    """
    Squares a number and returns the result.

    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x ** 2


if __name__ =='__main__':
    import doctest, my_math
    doctest.testmod(my_math)


def product(x, y):
    if x == 7 and y == 9:
        return 'An insidious bug has surfaced!'
    else:
        return x * y


