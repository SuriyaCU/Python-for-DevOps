import functools
import time
import random

class MaxRetriesExceededError(Exception):
    """Custom exception raised when a function fails after the maximum number of retries."""
    def __init__(self, attempts, last_exception):
        self.attempts = attempts
        self.last_exception = last_exception
        # Descriptive message for the parent Exception class
        message = f"Function failed after {attempts} attempts. Last error: {last_exception}"
        super().__init__(message)

def retry_with_backoff(max_attempts, base_delay=1.0, jitter=0.1):
    """
    A decorator factory for retrying a function with validation, exponential 
    backoff, jitter, and custom exceptions.
    """
    # 1. Factory Input Validation (with specific error messages for tests)
    if not isinstance(max_attempts, int) or max_attempts <= 0:
        raise ValueError("max_attempts must be a positive integer")
    
    if not (isinstance(base_delay, (int, float)) and base_delay >= 0):
        raise ValueError("base_delay must be a non-negative number")
        
    if not (isinstance(jitter, (int, float)) and jitter >= 0):
        raise ValueError("jitter must be a non-negative number")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    # Try to execute the wrapped function
                    return func(*args, **kwargs)
                
                except Exception as e:
                    last_exception = e
                    
                    # If we haven't reached the limit, wait before retrying
                    if attempt < max_attempts:
                        # Exponential Backoff: base_delay * 2^(attempt - 1)
                        # Plus random jitter: uniform(0, jitter)
                        wait_time = (base_delay * (2 ** (attempt - 1))) + random.uniform(0, jitter)
                        time.sleep(wait_time)
            
            # 2. If all attempts fail, raise custom error chained from the last actual exception
            raise MaxRetriesExceededError(max_attempts, last_exception) from last_exception
            
        return wrapper
    return decorator