"""
Use Case: ✅ Decorator Building Blocks with Closures
----------------------------------------------------
Closures are essential to building decorators, which wrap functions
to modify or extend their behavior.

🔧 Real-life Analogy:
Think of decorators like gift-wrapping: the original gift is inside,
but the wrapper adds a new appearance or behavior.

"""

def logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{message}] Calling function: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{message}] Result: {result}")
            return result
        return wrapper
    return decorator

@logger("DEBUG")
def add(a, b):
    return a + b

# Example usage
add(3, 4)  # ➜ Logs the function call and result
