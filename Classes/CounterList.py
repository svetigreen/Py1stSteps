class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0  # attribute (initially zero), which is incremented each time a list element is accessed

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


cl = CounterList(range(10))
print(cl)
print(cl.counter)
print(cl[4]+cl[2])
print(cl.counter)
print(cl[0]+cl[8])
print(cl.counter)
