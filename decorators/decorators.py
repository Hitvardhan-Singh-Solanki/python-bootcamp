# def returnOne():
#     return 1


# def hello(name="Jose"):
#     print(f"The function hello() has been executred with name={name}")

#     def greet():
#         return '\t This is a greet func inside hello'

#     def welcome():
#         return '\t This is a welcome func inside hello'

#     if name == 'Jose':
#         return greet
#     else:
#         return welcome


# returnOneCopy = returnOne

# del returnOne

# print(returnOneCopy())

# my_new_func = hello("Jose")

# print(my_new_func())

###########################################

# def hello():
#     return 'Hi Jose'


# def other(some_func):
#     print("Other code runs here")
#     print(some_func())


# other(hello)

##############################################

def new_decorator(orig_func):
    def wrap_func():
        print('Some extra code')
        orig_func()
        print('Some more extra code')
    return wrap_func


# decorated_func = new_decorator(fun_with_dec)

@new_decorator
def fun_with_dec():
    print('I want to be decorated')


fun_with_dec()
