import functools

def require_role(required_role):
    """
    A decorator factory that creates a decorator to check for a specific user role.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Extract the user dictionary from keyword arguments
            user = kwargs.get('user')
            
            # Check if the required_role exists in the user's roles list
            if required_role not in user.get('roles', []):
                raise PermissionError(
                    f"User '{user.get('name')}' does not have the "
                    f"required role: '{required_role}'"
                )
            
            # If authorized, execute and return the original function
            return func(*args, **kwargs)
            
        return wrapper
    return decorator

# --- Testing the implementation ---

@require_role('admin')
def restart_server(*, user, server_id):
    """Restarts a server after a permission check."""
    return f"Server {server_id} restart initiated by {user['name']}."

# Test Case 1: Authorized User
admin_user = {'name': 'alice', 'roles': ['admin', 'viewer']}
print(restart_server(user=admin_user, server_id='web-01'))

# Test Case 2: Unauthorized User (This will raise PermissionError)
# viewer_user = {'name': 'bob', 'roles': ['viewer']}
# restart_server(user=viewer_user, server_id='db-01')