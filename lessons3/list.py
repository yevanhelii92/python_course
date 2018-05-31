# task1
a1 = int (input('Число : '))

if a1 > 10 :
    print("bolshe ravno 10 \n this number is{}".format(a1))
elif 0 < a1 < 5  :
    print(a1 + 11)
    if a1 + 11 > 13:
        print("bolshe ravno 10 \n this number is{}".format(a1 + 11))
    else :
        print("bolshe ravno 10 \n this number is{}".format(a1 + 11))
else:
    if (a1 - 100)> -200 and a1 -100 < -50:
        print("between -200 and -50 \n this number is{}".format(a1 - 100))
    else :
        print("Fucking shit")


# task2
n = int (input('Число : '))
print("Fucking shit" * n )