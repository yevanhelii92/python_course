import time

def timer(func):
    def start_timer():
        start = time.time ()
        func()
        end = time.time()
        result = end - start
        print(result)
    return start_timer
@timer
def new_func ():
    for i in range(100000):
        i += 1


new_func()