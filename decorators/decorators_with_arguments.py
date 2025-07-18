# parameterized decorator

def conditional_log(enabled=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if enabled:
                print(f"{func.__name__} with {args}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@conditional_log(enabled=True)
def send_email(to, msg):
    return f"Sent to {to}"


send_email("Nikola", "Cao")
