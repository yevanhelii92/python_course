def my_decorator (func):
    def wraper():
        print ('cho to printani')
        func()
        print('cho to printani po novoy')
    return wraper
@my_decorator
def new_func ():
    print ('snova print new_func')
new_func()


