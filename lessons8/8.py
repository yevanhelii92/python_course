def func1 (pro = "Kruto"):
    return pro.upper() + '!!!'
def func2 (prop = "Shikarno"):
    return prop.upper() + '!!!!!!!!'
def do_before (func):
    print("do vizova func")
    print (func())
    print('posle vizova func')
do_before(func1)
print('='*100)
do_before(func2)