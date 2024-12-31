from functools import wraps

def authenticate(role='admin'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role == 'admin':
                func(*args, **kwargs)
            else:
                print('Доступ запрещён: требуется роль admin.')
        return wrapper
    return decorator


@authenticate(role='admin')
def delete_user(name, lst):
    '''Удаляет пользователя из списка'''
    lst.remove(name)
    print(f'Пользователь {name} удалён')

    
users = ['Harry', 'Hermiona', 'Ron', 'Luna', 'Newill', 'Draco']

delete_user('Newill', users)
print(users)
print(delete_user.__name__)
print(delete_user.__doc__)