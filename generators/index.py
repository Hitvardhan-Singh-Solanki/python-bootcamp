# generators.py

# Yeh hai aam zindagi
# def create_cubes(n):
#     result = []
#     for x in range(n+1):
#         result.append(x**3)
#     return result

# yeh hai mentos zidagi


def create_cubes(n):
    for x in range(n+1):
        yield x**3


def generateFib(n):
    if n < 2:
        return n
    return generateFib(n-1) + generateFib(n-2)


for i in range(10):
    print(generateFib(i))
