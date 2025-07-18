
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_args
def add(x, y):
    return x + y


print(add(3, 2))
