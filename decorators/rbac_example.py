# restrict functions based on their roles
# https://freedium.cfd/https://python.plainenglish.io/mastering-python-decorators-the-day-i-stopped-copy-pasting-code-forever-50349b74d131

user_role = "admin"  # could be "user", "guest", etc.


def require_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_role != role:
                return "Access Denied"
            return func(*args, **kwargs)
        return wrapper
    return decorator


@require_role("user")
def delete_user(user_id):
    return f"Deleted {user_id}"


delete_user(123)
