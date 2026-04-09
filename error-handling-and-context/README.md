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

