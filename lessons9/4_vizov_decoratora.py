from decorator.my_decorator import timer


@timer
def new_func ():
    for i in range(1000000):
        i += 1


new_func()