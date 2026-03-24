def read_config_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line


def filter_config_lines(lines):
    for line in lines:
        clean_line = line.strip()
        if clean_line and not clean_line.startswith('#'):
            yield clean_line


def parse_config_lines(lines):
    current_section = None

    for line in lines:
        # Section detection
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1].strip()
        
        else:
            # Always split safely
            key, value = line.split('=', 1)
            yield (current_section, key.strip(), value.strip())