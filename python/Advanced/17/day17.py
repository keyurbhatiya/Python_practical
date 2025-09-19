import time
from functools import wraps

# Function Decorator: Logs execution time
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Method Decorator: Checks if the user is authenticated
def authentication_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.is_authenticated:
            print("Access Denied! User is not authenticated.")
            return None
        return func(self, *args, **kwargs)
    return wrapper

# Example usage of function decorator
@timing_decorator
def compute_square(n):
    time.sleep(1)  # Simulate delay
    return n * n

# Example usage of method decorator
class User:
    def __init__(self, name, authenticated=False):
        self.name = name
        self.is_authenticated = authenticated
    
    @authentication_required
    def access_secure_data(self):
        print(f"Secure data accessed by {self.name}")

# Test function decorator
print(compute_square(5))

# Test method decorator
user1 = User("keyur", authenticated=True) # User is authenticated
user1.access_secure_data()

user2 = User("demo", authenticated=False) # User is not authenticated
user2.access_secure_data()
