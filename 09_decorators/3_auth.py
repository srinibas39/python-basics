from functools import wraps

def auth(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@auth
def access_inventory(role):
    print(f"Granted access to {role}")


access_inventory("user")
access_inventory("admin")
