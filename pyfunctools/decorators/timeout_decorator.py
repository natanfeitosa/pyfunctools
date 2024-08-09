import signal
from typing import Callable, Any, TypeVar

from pyfunctools.utils import is_func

C = TypeVar('C')


def timeout_decorator(seconds: int) -> Callable[[C], C]:
    """
    A decorator that raises a TimeoutError if the decorated function takes longer than a specified time to execute.

    Args:
        seconds (int): The maximum allowed time for the function to execute.

    Returns:
        Callable: The decorated function with timeout control applied.

    Examples:
        >>> @timeout_decorator(1)
        ... def func_test(say: str):
        ...     pass
        >>>
        >>> func_test('Something')
        Function func_test timed out after 1 seconds
        >>> @timeout_decorator(1)
        ... class MyClass:
        ...     def __init__(self, say: str):
        ...         pass
        >>>
        >>> MyClass('Something')
        Class MyClass timed out after 1 seconds
    """

    def decorator(func: C) -> C:
        def _handle_timeout(signum: int, frame: Any) -> None:
            obj_type = 'Class'

            if not is_func(func):
                obj_type = 'Function'

            raise TimeoutError(f"{obj_type} {func.__name__} timed out after {seconds} seconds")

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)

        return wrapper
    return decorator
