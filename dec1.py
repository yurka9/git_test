from functools import wraps

def log_calls(log_level='INFO'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{log_level} вызов функции {func.__name__} с аргументами: {args}')
            func(*args, **kwargs)
        return wrapper
    return decorator    

        
@log_calls(log_level='INFO')
def add(a, b):
    '''просто возвращает сумму двух чисел'''
    return a + b

add(2, 3)
print(add.__name__)
print(add.__doc__)