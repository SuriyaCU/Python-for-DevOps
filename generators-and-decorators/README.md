
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
