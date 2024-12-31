import time
from functools import wraps

def timer(unit='ms'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            st = time.time()
            func(*args)
            fn = time.time()
            if unit == 'ms':
                print(f'Время выполнения функции {func.__name__}: {(fn - st) * 10**6} ms')
            else:
                print(f'Время выполнения функции {func.__name__}: {fn - st} s')
        return wrapper
    return decorator


@timer(unit='ms')
def slow_function(t):
    '''создает задержку длинной t-секунд'''
    time.sleep(t)

slow_function(4)

print(slow_function.__name__)
print(slow_function.__doc__)

