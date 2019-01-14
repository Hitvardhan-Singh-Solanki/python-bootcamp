# List -> Array
# Dict -> Object
# Tuples -> Immutable arrays
# Sets -> set
# *args and **kwargs(Key word arguments)
# *args treas as tupes coming in as params


def myfunc(*args):
    return sum(args) * 0.05


def my_kwargs_func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('no Fruit')


print(myfunc(40, 60, 100, 200, 500))
my_kwargs_func(fruit='apple')
