import functools

class AuthorizationError(Exception):
    """Custom exception for RBAC failures."""
    def __init__(self, user_name, required_role):
        self.user_name = user_name
        self.required_role = required_role
        message = f"User '{user_name}' lacks the required role: '{required_role}'."
        super().__init__(message)

def require_role(required_role):
    """Decorator factory for Role-Based Access Control."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Validation Step 1: Check for keyword argument
            if 'user' not in kwargs:
                raise ValueError("A 'user' keyword argument is required")

            user = kwargs.get('user')

            # Validation Step 2: Check types and keys
            if not isinstance(user, dict):
                raise TypeError("'user' must be a dictionary")

            if 'roles' not in user:
                raise ValueError("'user' dictionary must contain a 'roles' key")

            if not isinstance(user['roles'], list):
                raise ValueError("'roles' must be a list")

            # Permission Check
            if required_role not in user['roles']:
                user_name = user.get('name', 'unknown')
                raise AuthorizationError(user_name, required_role)

            return func(*args, **kwargs)
        return wrapper
    return decorator