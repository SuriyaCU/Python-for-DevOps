import logging
import logging.config

def configure_logging(verbose: bool):
    """
    Configures logging dynamically based on a verbose flag.

    Args:
        verbose (bool): If True, sets the root logger level to DEBUG.
                        Otherwise, the level remains INFO.

    Returns:
        logging.Logger: The configured root logger instance.

    Raises:
        TypeError: If verbose is not a boolean.
    """
    # 1. Implement input validation
    if not isinstance(verbose, bool):
        raise TypeError("The 'verbose' argument must be a boolean.")

    # 2. Implement base logging config dictionary
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(levelname)s: %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }

    # 3. Modify the config dictionary based on the verbose parameter value
    if verbose:
        config['root']['level'] = 'DEBUG'

    # 4. Apply the configuration to the logging library
    logging.config.dictConfig(config)

    # 5. Return the configured root logger instance
    return logging.getLogger()