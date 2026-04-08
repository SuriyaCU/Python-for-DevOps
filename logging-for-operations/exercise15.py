import logging
from logging.handlers import RotatingFileHandler

def configure_rotating_logger(logger_name, log_filepath, max_size_bytes, backup_count):
    # --- Input Validation ---
    
    # Validate logger_name
    if not isinstance(logger_name, str):
        raise TypeError("logger_name must be a string.")
    if not logger_name.strip():
        raise ValueError("logger_name cannot be empty.")
        
    # Validate log_filepath
    if not isinstance(log_filepath, str):
        raise TypeError("log_filepath must be a string.")
    if not log_filepath.strip():
        raise ValueError("log_filepath cannot be empty.")
        
    # Validate max_size_bytes
    if not isinstance(max_size_bytes, int):
        raise TypeError("max_size_bytes must be an integer.")
    if max_size_bytes <= 0:
        raise ValueError("max_size_bytes must be greater than 0.")
        
    # Validate backup_count
    if not isinstance(backup_count, int):
        raise TypeError("backup_count must be an integer.")
    if backup_count < 0:
        raise ValueError("backup_count must be a non-negative integer.")

    # --- Logger Configuration ---
    
    # 1. Get the logger instance
    logger = logging.getLogger(logger_name)
    
    # 2. Set level to DEBUG to capture everything
    logger.setLevel(logging.DEBUG)
    
    # 3. Create the RotatingFileHandler
    handler = RotatingFileHandler(
        log_filepath, 
        maxBytes=max_size_bytes, 
        backupCount=backup_count
    )
    
    # Optional: Add a formatter so the logs are actually readable
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # 4. Add the handler to the logger
    # Note: In a production script, you might want to check if handlers 
    # already exist to avoid duplicate logs during re-configuration.
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger