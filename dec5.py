import random
import time
from functools import wraps

def retry(retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    res = func()
                    return res
                except Exception:
                    print('Функция завершилась с ошибкой')
                if i < retries - 1:
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(retries=3, delay=1)
def unstable_function():
    '''возвращает случайное число в диапазоне 0.0 - 1.0(не включая)'''
    if random.random() < 0.7:
        raise ValueError('Ошибка!')
    print('Успех!')

unstable_function()
print(unstable_function.__name__)
print(unstable_function.__doc__)