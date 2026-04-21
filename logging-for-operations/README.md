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
# Exercise 15: Log Rotator for a Monitoring Service

## Scenario
You are a **DevOps Engineer** responsible for a long-running system monitoring service. This service continuously writes status updates to a log file. To prevent this file from consuming all available disk space, you need to implement a log rotation strategy based on file size.

## Objective
Your task is to create a function `configure_rotating_logger` that sets up a logger to write to a file and automatically rotate it when it reaches a certain size.

## Functional Requirements
The function must accept four arguments:
* **logger_name** (str): The name for the logger.
* **log_filepath** (str): The path to the log file.
* **max_size_bytes** (int): The maximum size of the log file in bytes before it rotates.
* **backup_count** (int): The number of old log files to keep.

### Logic Requirements
1. **Logger Initialization:** Obtain a logger instance using the provided name and set its level to `DEBUG` to capture all messages.
2. **Handler Configuration:** Create and configure a `RotatingFileHandler` based on the provided arguments.
3. **Handler Attachment:** The handler must be added to the logger instance.
4. **Return Value:** The function must **return** the fully configured logger object.

### Input Validation
The function must strictly validate inputs and raise exceptions as follows:
* **logger_name** and **log_filepath**: Must be non-empty strings. Raise `ValueError` if empty, `TypeError` if not a string.
* **max_size_bytes** and **backup_count**: Must be integers. Raise `TypeError` if they are any other type.
* **max_size_bytes**: Must be greater than 0. Raise `ValueError` if not.
* **backup_count**: Must be a non-negative integer (0 or greater). Raise `ValueError` if negative.

---

## Example Usage

```python
# Configure a logger that rotates after ~1KB and keeps 3 backups.
log_path = "monitor_service.log"
service_logger = configure_rotating_logger(
    logger_name='monitoring_service',
    log_filepath=log_path,
    max_size_bytes=1024,
    backup_count=3
)

# This loop will eventually cause the log file to rotate.
for i in range(200):
    service_logger.info(f"Checking status of component {i}.")
```
---
# Exercise 16: Dynamic Logging Configuration with Verbose Mode

## Scenario
You are building a command-line tool for your team. To help with troubleshooting, you want to add a `--verbose` flag that increases the tool's log output. When the flag is present, the tool should log detailed `DEBUG` messages; otherwise, it should only show `INFO` level messages and higher.

## Objective
Your task is to implement a function, `configure_logging`, that sets up the application's logging based on a boolean flag. This function will define a base configuration as a dictionary and modify it dynamically before applying it to the system.

## Functional Requirements
The function must accept one argument:
* **verbose** (bool): A flag indicating whether to enable detailed logging.

### Logic Requirements
1.  **Base Configuration:** Inside the function, define a logging configuration dictionary. This dictionary should configure the **root logger** to use:
    * A `StreamHandler` (to output to the console).
    * A simple `Formatter` with the format: `%(levelname)s: %(message)s`.
    * A default log level of `INFO`.
2.  **Dynamic Modification:** * If the `verbose` argument is `True`, the function must programmatically modify the configuration dictionary to change the root logger's level to `DEBUG`.
    * If `verbose` is `False`, the configuration should remain at the default `INFO` level.
3.  **Application:** Apply the configuration using `logging.config.dictConfig()`.
4.  **Return Value:** The function must **return** the root logger instance.

### Input Validation
* If the `verbose` argument is not a boolean (`True` or `False`), the function must raise a `TypeError`.

---

## Example Usage

```python
# Scenario 1: Standard output
root_logger = configure_logging(verbose=False)
root_logger.debug("This will NOT be shown.")
root_logger.info("This WILL be shown.")

# Scenario 2: Verbose output
root_logger_v = configure_logging(verbose=True)
root_logger_v.debug("This WILL be shown now!")

---


