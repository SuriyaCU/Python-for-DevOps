import logging
import sys

def setup_script_logger(logger_name):
    """
    Configures and returns a logger for script activity monitoring.

    Args:
        logger_name (str): The name for the logger.

    Returns:
        logging.Logger: A configured logger instance.
    """
    # 1. Input Validation
    if not isinstance(logger_name, str):
        raise TypeError("logger_name must be a string.")
    
    if not logger_name.strip():
        raise ValueError("logger_name cannot be an empty string.")

    # 2. Create the Logger instance
    logger = logging.getLogger(logger_name)
    
    # Set the threshold level to INFO
    logger.setLevel(logging.INFO)

    # 3. Create a StreamHandler to send logs to the console
    console_handler = logging.StreamHandler(sys.stdout)

    # 4. Create a Formatter with the specified format
    # Format: <TIMESTAMP> - <LEVEL> - <MESSAGE>
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Add the Formatter to the Handler
    console_handler.setFormatter(log_format)

    # 5. Add the Handler to the Logger
    # Tip: Check if the logger already has handlers to avoid duplicate logs 
    # if the function is called multiple times for the same logger_name.
    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger