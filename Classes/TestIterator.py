class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
print(list(ti))
# Iterate over the instance to trigger __next__ and raise StopIteration
ti = TestIterator()
try:
    while True:
        print(next(ti))
except StopIteration:
    print("Iteration stopped.")
