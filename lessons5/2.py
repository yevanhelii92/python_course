def min100():
    if a1 < -100 or a1 >= 100:
        return a1 * 0
    else :
        return a1 + 1


assert min100(100) == 0, u"WTF"
print(min100(100))
