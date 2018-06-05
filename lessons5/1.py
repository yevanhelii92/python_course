def min10(a1):
    if -10 < a1 < 10:
        return a1 + 5
    else :
        return a1 - 10

assert min10(100) == 0, u"WTF"
print(min10(100))