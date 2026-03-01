def parse_log_line(log_line: str) -> dict | None:
    """
    Parses a single log line into a structured dictionary.
    """
    # 1. Validation: Check if input is a non-empty string
    if not isinstance(log_line, str) or not log_line.strip():
        return None

    # 2. Split the line into exactly 3 parts: timestamp, level, and message
    # Using maxsplit=2 ensures the message remains intact even if it contains spaces.
    parts = log_line.split(maxsplit=2)

    # Validate that we have all three required components
    if len(parts) < 3:
        return None

    timestamp, raw_level, message = parts

    # 3. Clean up the log_level and validate square brackets
    if not (raw_level.startswith('[') and raw_level.endswith(']')):
        return None
    
    log_level = raw_level.strip('[]')

    # 4. Return the structured dictionary
    return {
        'timestamp': timestamp,
        'log_level': log_level,
        'message': message
    }