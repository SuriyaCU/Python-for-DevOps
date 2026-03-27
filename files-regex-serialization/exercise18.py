import re

def has_critical_error(log_line: str) -> bool:
    """
    Checks if a log line contains a critical error indicator ('ERROR:' or 'FAIL:').
    The check is case-insensitive.

    Args:
        log_line (str): The log line to check.

    Returns:
        bool: True if a critical error indicator is found, False otherwise.
    """
    # Define a pattern for "ERROR:" or "FAIL:"
    # The | acts as an OR operator.
    pattern = r"ERROR:|FAIL:"

    # Use re.search to find the pattern anywhere in the string.
    # re.IGNORECASE makes it match error:, Fail:, ERROR:, etc.
    if re.search(pattern, log_line, re.IGNORECASE):
        return True
    
    return False

# --- Testing the logic ---
line1 = "2023-10-27 INFO: System started successfully."
line2 = "2023-10-27 ERROR: Database connection lost."
line3 = "2023-10-27 WARN: Disk usage high, but operation will not fail: all clear."
line4 = "2023-10-27 DEBUG: User 'test' initiated a fail: sequence."

print(f"Line 1: {has_critical_error(line1)}")  # Expected: False
print(f"Line 2: {has_critical_error(line2)}")  # Expected: True
print(f"Line 3: {has_critical_error(line3)}")  # Expected: False (no colon after fail)
print(f"Line 4: {has_critical_error(line4)}")  # Expected: True (contains fail:)