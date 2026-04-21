## Exercise 14: Basic Script Activity Logger

As a DevOps engineer, visibility into automation is critical. To ensure you can track what your scripts are doing in real-time, you need a standardized, reusable function to set up a logger for each script in your toolkit.

### Objective
Implement a function named `setup_script_logger` that creates, configures, and returns a logger object. This logger will send formatted messages to the console, making it easy to track a script's progress.

---

### Functional Requirements

### 1. Function Signature & Validation
The function must accept one argument: `logger_name` (a string).
* **TypeError**: Raise if `logger_name` is not a string.
* **ValueError**: Raise if `logger_name` is an empty string.

### 2. Configuration
* **Instance**: Get a logger instance using the provided `logger_name`.
* **Main Level**: The logger's level must be set to `INFO`.
* **Handler**: Send the log messages to the console via a `StreamHandler`.
* **Return**: The function must return the fully configured logger object.

### 3. Log Formatting
The format of the log lines must follow this structure:
`<TIMESTAMP> - <LEVEL> - <MESSAGE>`

> **Example:** `2026-03-25 10:30:00,123 - INFO - Script started.`

---

## Example Usage

```python
# In your main script
script_logger = setup_script_logger('deployment_script')
 
script_logger.debug("This is a debug message. It will not appear.")
script_logger.info("Starting deployment to production.")
script_logger.warning("Network latency is high.")
```

---
