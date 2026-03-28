
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


Expected Output

    (None, 'timeout', '30')
    ('database', 'host', 'db.prod.local')
    ('database', 'port', '5432')
    ('api_service', 'url', 'https://api.service.com/v1?retries=3')

---
