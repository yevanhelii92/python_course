a = lambda x, y: x == y
print(a(3, 5))

# подобное первой строке
def func1(x, y):
    return x == y
print(func1(3, 3))

# другой пример о lambda
print((lambda: [i for i in range(10) if i % 2 == 0])())
