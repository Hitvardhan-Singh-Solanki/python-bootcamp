def squ_are(num): return num ** 2


def check_even(num):
    return num % 2 == 0


lambda num: num ** 2

my_nums = [1, 3, 4, 2, 5]

# for item in map(squ_are, my_nums):
#     print(item)

# for i in filter(check_even, my_nums):
#     print(i)

print(list(map(
    lambda num: num ** 2, my_nums)))
