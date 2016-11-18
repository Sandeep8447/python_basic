def f(x, y):
    return x + y
print reduce(f, [1, 3, 5, 7, 9])

print reduce(lambda x,y: x+y, [1, 3, 5, 7, 9], 100)