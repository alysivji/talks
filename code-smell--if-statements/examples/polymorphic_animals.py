class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Dog(Animal):
    def speak(self):
        return "Woof!"
