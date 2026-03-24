import functools

def sanitize_hostname(func):
    """
    A decorator that finds a 'hostname' keyword argument, sanitizes it
    (lowercase, stripped whitespace), and passes it to the wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Access the hostname from kwargs
        hostname = kwargs.get('hostname')
        
        if hostname:
            # Apply sanitization: strip whitespace and convert to lowercase
            kwargs['hostname'] = hostname.strip().lower()
        
        # Call the original function with potentially modified kwargs
        return func(*args, **kwargs)
        
    return wrapper

# --- Testing the implementation ---

@sanitize_hostname
def connect_to_host(*, hostname):
    """Establishes a connection to a host."""
    print(f"Connecting to sanitized hostname: '{hostname}'")
    return f"Connected to {hostname}"

# Example Usage
result = connect_to_host(hostname="  PROD-API.local  ")
print(f"Return Value: {result}")
