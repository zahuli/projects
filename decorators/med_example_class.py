# https://blog.stackademic.com/python-unleashing-the-magic-1-decorators-b70c1bc4dae7

class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Code to be executed before the original function
        print("Decorator class: Before function execution")

        # Call the original function
        result = self.func(*args, **kwargs)

        # Code to be executed after the original function
        print("Decorator class: After function execution")

        return result

@DecoratorClass
def decorated_function():
    print("Original function")

# Using the decorated function
decorated_function()