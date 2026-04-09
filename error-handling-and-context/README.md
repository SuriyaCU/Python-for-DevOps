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

