from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def introduce(self):
        pass

    def move(self):
        print("Moving...")


class Dog(Animal):
    def make_sound(self):
        print("Bark")

    def introduce(self):
        print("I'm a dog")


class Cat(Animal):
    def make_sound(self):
        print("Meow")

    def introduce(self):
        print("I'm a cat")


class Cow(Animal):
    def make_sound(self):
        print("Muuuuh")

    def introduce(self):
        print("I'm a cow")


# Example usage
for animal in (Dog(), Cat(), Cow()):
    animal.introduce()
    animal.make_sound()
    animal.move()
