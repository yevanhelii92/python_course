from random import randint

a = 6
b = 6
def kubik ():
    n=1
    while True:
        a = randint (1, 6)
        b = randint (1, 6)
        if a + b == 8 :
            print (a, b, n)
            break
        n += 1
kubik()
