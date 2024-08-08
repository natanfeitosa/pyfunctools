import time
from functools import wraps


def retry_decorator(retries=3, delay=2):
    """
    A decorator to retry a function execution upon failure.

    This decorator retries the execution of the decorated function
    a specified number of times, with a delay between each attempt,
    in case of an exception.

    Args:
        retries (int): The number of retry attempts. Default is 3.
        delay (int): The delay between retries in seconds. Default is 2.

    Returns:
        callable: A function that retries the original function upon failure.

    Example:
        >>> @retry_decorator(retries=5, delay=1)
        ... def flaky_function():
        ...     import random
        ...     if random.choice([True, False]):
        ...         raise ValueError("Oops, something went wrong!")
        ...     return "Success!"
        >>>
        >>> print(flaky_function())
        "Success!" # (or an exception after retries)
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time.sleep(delay)
            raise last_exception

        return wrapper

    return decorator
