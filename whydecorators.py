# Decorator
from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t1-t2} s')
        return result
    return wrapper

@logging
def long_time():
    for i in range(100000000):
        i*5

long_time()


