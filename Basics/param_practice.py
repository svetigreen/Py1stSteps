def story(**kwds):
    return 'Once upon a time, there was a ' \
           '{job} called {name}. He was {age} year old. '.format_map(kwds)


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:  # If the stop is not supplied ...
        start, stop = 0, start  # shuffle the parameters
    result = []
    i = start  # We start counting at the start index
    while i < stop:  # Until the index reaches the stop index ...
        result.append(i)  # ... append the index to the result ...
        i += step  # ... increment the index with the step (> 0)
    return result


def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor  # One function is inside another, and the outer function returns the inner one;
        # that is, the function itself is returned—it is not called.
    return multiplyByFactor


print(story(job='king', name='Gumby', age=42))

power(3, 3, 'Hello, world')

power(*interval(3, 7))

triple = multiplier(3)
print(triple(3))
print(multiplier(5)(4))
