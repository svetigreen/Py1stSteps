class Person:

    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def greet(self):
        print("Hello, I'm {}.".format(self._name))


p1 = Person("Anna")
p1.greet()

p2 = Person()
p2.name = "Bob"
p2.greet()

