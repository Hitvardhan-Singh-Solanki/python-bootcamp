class Dog():

    # class object attribute
    # Will not change for a new instance
    species = 'mammal'

    # constructor
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # method
    def bark(self):
        print('woof')


my_dog = Dog('pomaranian', 'ginger')
my_dog.bark()
print(my_dog.breed, my_dog.name, my_dog.species)
