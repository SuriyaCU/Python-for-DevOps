import re
from typing import Optional

def parse_login_event(log_line: str) -> Optional[dict[str, str]]:
    """
    Parses a login event log line to extract the username and status.

    Args:
        log_line (str): The log line to parse.

    Returns:
        A dictionary with 'username' and 'status' if the line matches,
        otherwise None.
        
    Raises:
        TypeError: If log_line is not a string.
    """
    # 1. Input validation
    if not isinstance(log_line, str):
        raise TypeError("log_line must be a string")
    
    # 2. Define the regex pattern with named groups
    # (?P<username>[^']+) matches one or more characters that are NOT a single quote
    # (?P<status>\w+) matches the status word (e.g., SUCCESSFUL)
    # The \. at the end matches the literal period
    pattern = r"LOGIN_EVENT: User '(?P<username>[^']+)' login attempt was (?P<status>\w+)\."
    
    # 3. Match the pattern against the input
    match = re.search(pattern, log_line)
    
    # 4. Return the dictionary of named groups if found, else None
    if match:
        return match.groupdict()
    
    return None

# --- Testing the logic ---
log1 = "LOGIN_EVENT: User 'jdoe' login attempt was SUCCESSFUL."
log2 = "LOGIN_EVENT: User 'admin' login attempt was FAILED."
log3 = "INFO: Application started."

print(parse_login_event(log1))  # {'username': 'jdoe', 'status': 'SUCCESSFUL'}
print(parse_login_event(log2))  # {'username': 'admin', 'status': 'FAILED'}
print(parse_login_event(log3))  # None