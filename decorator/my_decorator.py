import time

def timer(func):
    def start_timer():
        start = time.time ()
        func()
        end = time.time()
        result = end - start
        print(result)
    return start_timer