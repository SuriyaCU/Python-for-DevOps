def read_log_lines(filepath):
    """
    Creates a generator that reads a log file, yielding valid, non-comment lines.

    Args:
        filepath (str): The path to the log file.

    Yields:
        str: A stripped, non-empty, non-comment line from the file.
    """
    # Using 'with' ensures the file is closed automatically even if an error occurs
    with open(filepath, 'r') as file:
        for line in file:
            # 1. Remove leading/trailing whitespace
            stripped_line = line.strip()
            
            # 2. Skip empty lines
            if not stripped_line:
                continue
            
            # 3. Skip comment lines (starts with # after stripping)
            if stripped_line.startswith('#'):
                continue
            
            # 4. If it passes all checks, yield the processed line
            yield stripped_line