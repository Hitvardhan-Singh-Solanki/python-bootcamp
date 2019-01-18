def simple_gen():
    for x in range(3):
        yield x


g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
