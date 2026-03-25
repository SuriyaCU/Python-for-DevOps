
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


Expected Output

    (None, 'timeout', '30')
    ('database', 'host', 'db.prod.local')
    ('database', 'port', '5432')
    ('api_service', 'url', 'https://api.service.com/v1?retries=3')

---
