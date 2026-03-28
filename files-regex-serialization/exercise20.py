import re

def redact_sensitive_data(content: str) -> str:
    """
    Finds and redacts sensitive values (api_key, password, secret) in a string.

    Args:
        content (str): The string content to be sanitized.

    Returns:
        str: The content with sensitive values replaced by '[REDACTED]'.
    
    Raises:
        TypeError: If content is not a string.
    """
    # 1. Input validation
    if not isinstance(content, str):
        raise TypeError("Content must be a string.")

    # 2. Define the regex pattern
    # (api_key|password|secret) -> Matches any of the three keys (Group 1)
    # \s*[:=]\s* -> Matches optional whitespace, then : or =, then optional whitespace (Group 2)
    # .+                        -> Matches the actual value (the part we want to replace)
    # re.IGNORECASE             -> Makes the keys case-insensitive
    # re.MULTILINE              -> Ensures ^ matches the start of each line
    pattern = r"^(api_key|password|secret)(\s*[:=]\s*).+"
    
    # 3. Define the replacement
    # \1 refers to the first captured group (the key)
    # \2 refers to the second captured group (the separator and whitespace)
    replacement = r"\1\2[REDACTED]"

    # 4. Perform the substitution
    redacted_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.MULTILINE)
    
    return redacted_content

# --- Example Usage ---
file_content = """# Application Settings
host = web.service.local
api_key = "abc-123-def-456"
retries = 3

# Database Credentials
Password: mySuperSecretPassword!
user = admin"""

print(redact_sensitive_data(file_content))