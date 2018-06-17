# oblast vidimosti
x = 1
y = 1
z = 1
def outer():
    global z
    x = 10
    z = 10
    def inner():
        # nonlocal z
        z = 100
        print('x in inner = ', x)
        print('y in inner = ', y)
        print('z in inner = ', z)
    inner()
    print(z)
outer()
print(x, y, z)