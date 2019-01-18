# Parent class
class Animal():
    def __init__(self):
        print("animal created")

    def eat(self):
        print("I am eating")
        return 0

    def who_am_i(self):
        print("I am an Animal")


# Derieved class


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")


my_dog = Dog().eat()
