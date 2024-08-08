from functools import wraps
from concurrent.futures import ThreadPoolExecutor


def threaded_decorator(func):
    """
    A decorator to run a function in a separate thread.

    This decorator uses a ThreadPoolExecutor to run the decorated
    function in a separate thread, allowing for concurrent execution.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: A function that runs the original function in a thread.

    Example:
        >>> @threaded_decorator
        ... def slow_function(x):
        ...     import time
        ...     time.sleep(2)
        ...     return x * 2
        >>>
        >>> print(slow_function(5))
        10
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(func, *args, **kwargs)
            return future.result()
    return wrapper
