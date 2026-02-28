def validate_config(config: dict) -> bool:
    """
    Validates a configuration dictionary against a set of rules.
    """
    # 1. Check if all required keys exist
    required_keys = ['service_name', 'env', 'port']
    for key in required_keys:
        if key not in config:
            return False

    # 2. Check if the 'env' value is one of 'dev', 'staging', 'prod'
    allowed_envs = ['dev', 'staging', 'prod']
    if config['env'] not in allowed_envs:
        return False

    # 3. Check if 'service_name' is a non-empty string
    service_name = config['service_name']
    if not isinstance(service_name, str) or service_name == "":
        return False

    # 4. Check if 'port' is an integer and within 1-65535 (inclusive)
    port = config['port']
    # Ensure port is an int but NOT a boolean (since bools are ints in Python)
    if not isinstance(port, int) or isinstance(port, bool):
        return False
    
    if not (1 <= port <= 65535):
        return False

    # If all checks pass, return True
    return True