## Exercise 10: Validating Inputs for Flexible Resource Tagger

### 🚀 Context
In production DevOps environments, functions rarely receive "perfect" data. A utility like a **Resource Tagger** might be used by various CI/CD scripts or other developers. If the function expects a dictionary but receives a string or `None`, it could crash the entire deployment pipeline.

This exercise focuses on **Input Validation** and **Defensive Programming**—ensuring our function "fails fast" with a descriptive error before attempting any logic.

### 📝 Objective
Harden the `manage_tags` function by adding a validation layer. The function must verify that the initial set of tags is a dictionary before proceeding with any additions or removals.

### Behavioral Requirements
* **Type Checking:** Use `isinstance()` to verify that `existing_tags` is a dictionary (`dict`).
* **Exception Handling:** If the input is invalid (e.g., a string, list, or `None`), raise a `TypeError`.
* **Descriptive Errors:** The error message should clearly state what was expected versus what was received.
* **Logic Preservation:** If validation passes, the function should continue to process tag additions and removals as per previous requirements.

---

### 🛠️ Implementation

```python
def manage_tags(existing_tags, **kwargs):
    """
    Manages resource tags by adding or updating based on keyword arguments.
    Validates that the initial input is a dictionary.
    """
    
    # 1. Input Validation
    if not isinstance(existing_tags, dict):
        raise TypeError(
            f"Expected 'existing_tags' to be a dict, but received {type(existing_tags).__name__}."
        )

    # 2. Core Logic (Processing Tags)
    # We create a copy to avoid unintended side effects on the original dict
    updated_tags = existing_tags.copy()
    
    for key, value in kwargs.items():
        if value is None:
            # If value is None, remove the tag if it exists
            updated_tags.pop(key, None)
        else:
            # Otherwise, add or update the tag
            updated_tags[key] = value
            
    return updated_tags
```
## --- Example Usage ---

if __name__ == "__main__":
    current_tags = {"env": "prod", "service": "web"}
    
    # Successful execution
    new_tags = manage_tags(current_tags, service="api", owner="devops")
    print(f"Updated Tags: {new_tags}")

    # Triggering the TypeError
    try:
        manage_tags(["env", "prod"], version="1.0")
    except TypeError as e:
        print(f"Validation Caught: {e}")

---

## Exercise 11: Validating Inputs for Object-Oriented Deployment Manager

## 🚀 Context
As a Senior DevOps Engineer, your code often serves as the backbone for automation. A `Deployment` class that "blindly trusts" its inputs is a liability. If a script passes an integer instead of a string for a `service_name`, or an empty string for a `new_version`, the system should fail **fast and loudly** before any actual infrastructure changes occur.

This exercise focuses on hardening our previously built `Deployment` class using **Exception Handling** to ensure data integrity.

### 📝 Objective
Modify the `Deployment` class to include robust input validation in both the constructor (`__init__`) and the `deploy` method. The goal is to catch `TypeError` and `ValueError` scenarios immediately.

### Behavioral Requirements

#### 1. Constructor Validation (`__init__`)
* **TypeError:** Raise if `service_name` or `environment` are not strings.
* **ValueError:** Raise if `service_name` or `environment` are empty strings (after stripping whitespace).

#### 2. Method Validation (`deploy`)
* **TypeError:** Raise if `new_version` is not a string.
* **ValueError:** Raise if `new_version` is an empty string.

---

### 🛠️ Implementation

```python
class Deployment:
    def __init__(self, service_name, environment):
        # 1. Validate service_name
        if not isinstance(service_name, str):
            raise TypeError(f"service_name must be a string, got {type(service_name).__name__}")
        if not service_name.strip():
            raise ValueError("service_name cannot be an empty string")

        # 2. Validate environment
        if not isinstance(environment, str):
            raise TypeError(f"environment must be a string, got {type(environment).__name__}")
        if not environment.strip():
            raise ValueError("environment cannot be an empty string")

        self.service_name = service_name
        self.environment = environment
        self.version = "v0.0.0"
        self.prev_version = None

    def deploy(self, new_version):
        # 3. Validate new_version
        if not isinstance(new_version, str):
            raise TypeError(f"new_version must be a string, got {type(new_version).__name__}")
        if not new_version.strip():
            raise ValueError("new_version cannot be an empty string")

        self.prev_version = self.version
        self.version = new_version
        print(f"Deployed {self.service_name} {new_version} to {self.environment}")

    def rollback(self):
        if self.prev_version:
            print(f"Rolling back {self.service_name} to {self.prev_version}")
            self.version, self.prev_version = self.prev_version, None
        else:
            print(f"No previous version found for {self.service_name}")

    def check_status(self):
        return f"{self.service_name} is running {self.version} in {self.environment}"
```
## --- Example Usage ---
try:
    # This will trigger a ValueError
    bad_deploy = Deployment("", "production")
except ValueError as e:
    print(f"Caught expected error: {e}")

try:
    # This will trigger a TypeError
    app = Deployment("api-service", "prod")
    app.deploy(1.2) # Passing a float instead of a string
except TypeError as e:
    print(f"Caught expected error: {e}")

---
## Exercise 12: Robust RBAC Decorator with Custom Exceptions

### Scenario
This exercise builds on the Role-Based Access Control (RBAC) decorator. In a production system, you cannot assume that inputs (like user objects) will always be well-formed. To make the system reliable, your decorator must validate its inputs and provide clear, domain-specific errors using custom exceptions.

### Objective
Enhance the `require_role` decorator factory by adding strict input validation and a custom exception class named `AuthorizationError`.

### Functional Requirements

#### 1. Define a Custom Exception
Create a class named `AuthorizationError` that inherits from `Exception`.
* **Initialization:** The `__init__` method must accept `user_name` and `required_role`.
* **Attributes:** Store these values as attributes on the instance.
* **Message:** Generate a clear error message, e.g., `"User 'alice' lacks the required role: 'admin'."`

#### 2. Enhance the Decorator Factory
Modify the `require_role` decorator's internal wrapper to perform validation **before** checking permissions:

* **Validation Step 1 (Missing Argument):** If the `user` keyword argument is missing from the function call, raise a `ValueError`.
* **Validation Step 2 (Type Check):** If the `user` argument is provided but is not a `dict`, raise a `TypeError`.
* **Validation Step 3 (Malformed Dictionary):** If the `user` dictionary is missing the `roles` key, or if `user['roles']` is not a `list`, raise a `ValueError`.
* **Permission Check:** If all validations pass but the user lacks the required role, raise the custom `AuthorizationError` (instead of a generic `PermissionError`).

---

### Example Usage

```python
# Custom exception for clarity
class AuthorizationError(Exception):
    # ... implementation ...
    pass

@require_role('admin')
def restart_server(*, user, server_id):
    """Restarts a server after a permission check."""
    return f"Server {server_id} restart initiated."

admin_user = {'name': 'alice', 'roles': ['admin']}
viewer_user = {'name': 'bob', 'roles': ['viewer']}
malformed_user = {'name': 'eve'} # Missing 'roles' key

# Succeeds:
restart_server(user=admin_user, server_id='web-01')

# Raises AuthorizationError:
# restart_server(user=viewer_user, server_id='db-01')

# Raises ValueError (Malformed input):
# restart_server(user=malformed_user, server_id='app-01')

# Raises ValueError (Missing keyword argument):
# restart_server(server_id='app-01')

---
## Exercise 13: Advanced Retry Decorator with Exponential Backoff and Jitter

### Scenario
You are a **DevOps Engineer** writing scripts that interact with a critical but occasionally flaky API. When the API has a momentary outage, all client scripts often retry at the exact same time, causing a "thundering herd" effect that overloads the API as soon as it comes back online. To solve this, you need a decorator that spaces out retries intelligently.

### Objective
Implement a robust, production-ready retry decorator factory named `retry_with_backoff`. This decorator must use **exponential backoff** and **random jitter** to spread out retry attempts and provide clear, contextual errors upon final failure.

### Functional Requirements

### 1. Decorator Factory Arguments
The factory must accept three arguments:
* `max_attempts` (int): Total number of times to try the function.
* `base_delay` (float/int): The starting delay duration.
* `jitter` (float/int): The maximum random noise to add to the delay.

### 2. Retry Logic
* **Success:** If the wrapped function succeeds, return its value immediately.
* **Exponential Backoff:** If the function raises an `Exception`, the delay before the next retry should follow the formula:  
    `delay = base_delay * (2 ** (failure_count - 1))`
* **Random Jitter:** To prevent synchronized retries, add a random value between `0` and `jitter` (using `random.uniform(0, jitter)`) to each calculated delay.
* **Metadata:** The decorator must preserve the original function's metadata (e.g., `__name__`, `__doc__`).

### 3. Custom Exception: `MaxRetriesExceededError`
Define a custom exception class that inherits from `Exception`:
* **Initialization:** The `__init__` method must accept `attempts` (total attempts made) and `last_exception` (the final error caught).
* **Attributes:** Store these values as attributes on the instance.
* **Final Failure:** If the function fails all `max_attempts`, raise `MaxRetriesExceededError` **from** the last exception caught (using `raise ... from ...`) to preserve exception chaining.

### 4. Input Validation
The `retry_with_backoff` factory must validate its own arguments when it is first called:
* `max_attempts` must be an integer greater than 0.
* `base_delay` and `jitter` must be non-negative numbers (0 or greater).
* Raise a `ValueError` if any validation fails.

---

### Example Usage

```python
class MaxRetriesExceededError(Exception):
    # ... implementation ...
    pass

@retry_with_backoff(max_attempts=3, base_delay=0.1, jitter=0.05)
def connect_to_api():
    """Simulates a network call that might fail."""
    print("Attempting to connect...")
    raise ConnectionError("API Offline")

try:
    connect_to_api()
except MaxRetriesExceededError as e:
    print(f"Failed after {e.attempts} attempts.")
    print(f"The underlying cause was: {e.last_exception}")
```
---

