class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError(f"Attribute '{name}' not found")


r = Rectangle()
r.width = 10
r.height = 5
print(f'Width: ', r.width)
print(f'Height: ', r.height)
print(f'Size: ', r.size)

r.size = 50, 30
print(f'Width: ', r.width)
print(f'Height: ', r.height)
print(f'Size: ', r.size)

try:
    print(f'Volume: ', r.volume)
except AttributeError as e:
    print(e)

