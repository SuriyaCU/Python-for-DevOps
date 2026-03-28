
## Exercise 6: Log File Line Generator

### The Task
You are a DevOps engineer tasked with creating a memory-efficient tool for parsing large log files. A full-featured log parsing library might be too heavy, and loading a multi-gigabyte file into memory would be inefficient.

Your goal is to write a Python **generator function** named `read_log_lines` that reads a log file line by line, yielding only the valid log entries.

### Requirements

- **Function Signature:** The function must accept a single argument: `filepath` (a string).
- **Memory Efficiency:** Your function **must be a generator**. It must use the `yield` keyword and should **not return a list or any other collection**.
- **Input Handling:** It must open and read the file specified by `filepath`.

### Validation Rules

- **Valid Log Lines:** Yield each valid log line. A valid line is any line that is **not empty** and **not a comment**.
- **Comment Lines:** Lines starting with a `#` character are comments. Whitespace before the `#` should be ignored (for example: `   # comment`).
- **Whitespace:** Empty lines or lines containing only whitespace should be skipped.
- **Sanitization:** Each yielded line must have **leading and trailing whitespace removed**.

### Example Scenario

Given a file named **`sample.log`** with the following content:

```text
[INFO] Application starting...
[DEBUG] Connecting to database.
 
# Configuration section
  # A nested comment
[WARN] Deprecated feature used.
```

---

## Exercise 7: Configuration File Processing Pipeline

### Problem Statement

You are a DevOps engineer responsible for building a tool that processes large configuration files efficiently using **generators**.


### Configuration File Format

* Sections are defined using square brackets like: [database]
* Key-value pairs are defined as: key = value
* Comments start with #
* Empty lines should be ignored


### Objective

Build a pipeline of three generator functions to process configuration files lazily.


### Functions to Implement

#### 1. read_config_file(filepath)
* Accepts a file path
* Opens the file
* Yields each line one by one


#### 2. filter_config_lines(lines)
* Accepts an iterable of lines
* Strips whitespace
* Ignores:
  * Empty lines
  * Lines starting with #
* Yields only valid lines



#### 3. parse_config_lines(lines)
* Accepts cleaned lines
* Tracks current section (None initially)

Behavior:
* If line is a section like [section]:
  * Update current section
  * Do not yield anything
* If line is a key-value pair:
  * Split using split('=', 1)
  * Yield (current_section, key, value)


### Example

Input (app.cfg)

    # Global settings
    timeout = 30

    [database]
    host = db.prod.local
    port = 5432

    [api_service]
    url = https://api.service.com/v1?retries=3

---
## Exercise 8: Argument Sanitizer Decorator

### 🚀 Context
In DevOps automation, data consistency is critical. When interacting with cloud infrastructure, APIs, or SSH clients, hostnames must often follow a strict format. Instead of manually cleaning strings inside every function, this exercise demonstrates how to use **Python Decorators** to centralize sanitization logic.

### 📝 Objective
Create a decorator named `sanitize_hostname` that automatically intercepts the `hostname` keyword argument, converts it to lowercase, and strips any leading or trailing whitespace before the decorated function executes.

### Functional Requirements
* **Universal Compatibility:** The wrapper must accept arbitrary positional (`*args`) and keyword (`**kwargs`) arguments.
* **Targeting:** Specifically look for the `hostname` key within the `kwargs` dictionary.
* **Sanitization:** Convert the value to lowercase and remove surrounding whitespace.
* **Execution:** Call the original function with the sanitized arguments and return its original return value.
* **Metadata:** Use `functools.wraps` to preserve the original function’s metadata (like `__name__` and `__doc__`).

---

### 🛠️ Implementation

```python
import functools

def sanitize_hostname(func):
    """
    A decorator that finds a 'hostname' keyword argument, sanitizes it
    (lowercase, stripped whitespace), and passes it to the wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Look for the 'hostname' key in the keyword arguments
        hostname = kwargs.get('hostname')
        
        if hostname:
            # 2. Apply sanitization: remove whitespace and lowercase
            kwargs['hostname'] = hostname.strip().lower()
        
        # 3. Execute the original function with the updated kwargs
        return func(*args, **kwargs)
        
    return wrapper
```

## --- Example Usage ---

@sanitize_hostname
def connect_to_host(*, hostname):
    """Establishes a connection to a host."""
    print(f"Connecting to sanitized hostname: '{hostname}'")
    return f"Connected to {hostname}"

if __name__ == "__main__":
    # Test: The decorator will sanitize '  PROD-API.local  ' to 'prod-api.local'
    result = connect_to_host(hostname="  PROD-API.local  ")
    print(f"Function Result: {result}")

---

## Exercise 9: Role-Based Access Control (RBAC) Decorator Factory

### 🚀 Context
As a DevOps engineer, you are often tasked with building internal tools that perform sensitive operations (e.g., restarting production servers, clearing databases, or modifying cloud permissions). Security is paramount, and manually adding permission checks to every function is error-prone and repetitive.

In this exercise, we implement a **Decorator Factory**. This allows us to create a configurable decorator that can be used across multiple functions to enforce specific role requirements.

### 📝 Objective
Create a decorator factory named `require_role`. This factory accepts a `required_role` string and generates a decorator that verifies if a user has the necessary permissions before allowing a function to execute.

### Functional Requirements
* **The Factory:** `require_role(required_role)` must return a decorator function.
* **The Wrapper:** * Must accept arbitrary positional (`*args`) and keyword (`**kwargs`) arguments.
    * Must extract the `user` dictionary from the keyword arguments.
* **Logic:**
    * Check if `required_role` exists within the user's `roles` list.
    * If the role is missing, raise a `PermissionError`.
    * If the role exists, execute the function and return its value.
* **Metadata:** Use `functools.wraps` to ensure the original function’s name and docstring are preserved.

---

### 🛠️ Implementation

```python
import functools

def require_role(required_role):
    """
    A decorator factory that creates a decorator to check for a specific user role.

    Args:
        required_role (str): The role string that the user must have.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 1. Retrieve the user dictionary from kwargs
            user = kwargs.get('user')
            
            # 2. Check if the user has the required role
            # (Assuming user['roles'] is always a list per requirements)
            if required_role not in user.get('roles', []):
                raise PermissionError(
                    f"Access Denied: User '{user.get('name')}' lacks the '{required_role}' role."
                )
            
            # 3. If check passes, execute and return the original function
            return func(*args, **kwargs)
            
        return wrapper
    return decorator
```

## --- Example Usage ---

@require_role('admin')
def restart_server(*, user, server_id):
    """Restarts a server after a permission check."""
    return f"Server {server_id} restart initiated by {user['name']}."

if __name__ == "__main__":
    admin_user = {'name': 'alice', 'roles': ['admin', 'viewer']}
    viewer_user = {'name': 'bob', 'roles': ['viewer']}

    # Successful call
    print(restart_server(user=admin_user, server_id='web-01'))

    # This would raise PermissionError
    # print(restart_server(user=viewer_user, server_id='db-01'))

---


Expected Output

    (None, 'timeout', '30')
    ('database', 'host', 'db.prod.local')
    ('database', 'port', '5432')
    ('api_service', 'url', 'https://api.service.com/v1?retries=3')

---
