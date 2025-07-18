# Class-Based Decorators

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f"Call {self.counter} to {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def greet(name):
    return f"Hello {name}"


greet("Alice")
greet("Bob")
