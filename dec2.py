from functools import wraps

def limit_call(max_calls=3):
    def decorator(func):
        counter = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter
            if counter < max_calls:
                func()
                counter += 1
            else: 
                print(f'Ошибка: превышено максимальное количество вызовов {max_calls}')

        return wrapper
    return decorator


@limit_call(3)
def greet():
    '''выводит приветствие'''
    print('Hello!')

greet()
greet()
greet()
greet()
print(greet.__name__)
print(greet.__doc__)