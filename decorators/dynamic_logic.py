def math_operation(op):
    def decorator(func):
        def wrapper(*args):
            if op == "square":
                return [x ** 2 for x in args]
            elif op == "double":
                return [x * 2 for x in args]
            return func(*args)
        return wrapper
    return decorator


@math_operation("double")
def process_numbers(*args):
    return args


print(process_numbers(1, 2, 3))
