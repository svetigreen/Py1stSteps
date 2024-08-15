class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()
# Print out the first 100 Fibonacci numbers
print("First 20 Fibonacci numbers:")
for _ in range(20):
    print(next(fibs), end=' ')
print("\n")

# Create a new instance of the Fibs class for the second loop
fibs = Fibs() # otherwise it will iterate from the position on it finished before
# Print out the smallest Fib number that is greater than 1000
print("First Fibonacci number greater than 1000:")
for f in fibs:
    if f > 1000:
        print(f)
        break

