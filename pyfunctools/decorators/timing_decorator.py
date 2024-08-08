import time
import typing as t
from functools import wraps

__all__ = ('timing_decorator',)


def timing_decorator(log_func: t.Callable[[str, float, float], t.Any] = None):
    """
    A decorator to measure the execution time of a function.

    This decorator measures the time taken by the decorated function to
    execute and logs the start time, end time, and duration. It can use
    a custom logging function if provided; otherwise, it defaults to printing.

    Args:
        log_func (t.Callable[[str, float, float], t.Any], optional): A custom logging function that accepts
                                       three arguments: the function name,
                                       start time, and end time. If not provided,
                                       it defaults to printing the information.

    Returns:
        callable: A function that measures the execution time of the original function.

    Example:
        >>> def custom_logger(func_name, start_time, end_time):
        ...     print(f'{func_name} started at * and ended at *, taking * seconds')
        >>>
        >>> @timing_decorator(log_func=custom_logger)
        ... def example_function(x):
        ...     time.sleep(2)
        ...     return x * 2
        >>>
        >>> print(example_function(5))
        example_function started at * and ended at *, taking * seconds
        10
    """
    if log_func is None:
        def log_func(fn_name, starts, ends):
            print(f"{fn_name} took {ends - starts:.4f} seconds")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            log_func(func.__name__, start_time, end_time)
            return result

        return wrapper

    return decorator
