def shall(word = "yes"):
    return word.upper() + '!!!'
script = shall
print(script())

del shall
try:
    print(shall())
except NameError as qwe:
    print(qwe)
print(shall())