from flask import session

from functools import wraps

def check_logged_in(func): # check_logged_in 修饰符有一个参数：被修饰函数的函数对象
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in'
    return wrapper