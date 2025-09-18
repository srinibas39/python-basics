#  Takes the functions as arguments and adds some functionality before or after the function call.

from functools import wraps

def my_decorator(func):
    @wraps(func) #changes metadata like function name of argument function  
    def wrapper():
         print("Before function call")
         func()
         print("After function call")
    return wrapper

@my_decorator
def func():
    print("Hello from decorators")

func()

print(func.__name__)
