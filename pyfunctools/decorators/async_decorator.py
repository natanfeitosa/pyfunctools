import asyncio
import typing
from functools import wraps

__all__ = ('async_decorator',)


def async_decorator(func: typing.Callable[[typing.Any], typing.Any]):
    """
    A decorator to run a synchronous function asynchronously using asyncio.

    This decorator converts a blocking function into an async function
    by running it in an executor. It uses the asyncio event loop to
    handle the execution.

    Args:
        func (callable): The synchronous function to be decorated.

    Returns:
        callable: An async function that wraps the original function.

    Example:
        >>> import time
        >>> @async_decorator
        ... def blocking_function(x):
        ...     import time
        ...     time.sleep(2)
        ...     return x * 2
        >>> async def main():
        ...     result = await blocking_function(5)
        ...     print(result)
        >>> asyncio.run(main())
        10
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, lambda: func(*args, **kwargs))
        return result

    return wrapper
