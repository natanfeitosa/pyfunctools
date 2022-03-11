from functools import wraps
from pyfunctools.utils import is_func

def memoize(func):
    """Creates a cache of the returns and arguments received by a function passed by parameter

    Args:
        func ( function ) : function to generate the cache

    Raises:
        TypeError:
            thrown when func is not a valid function

    Examples:
        >>> fat = memoize(lambda n: 1 if n == 0 else n * fat(n-1))
        >>> fat(4)
        24
        >>> @memoize
        >>> def sums(*numbers):
                '''Receives a numeric sequence and calculates the sum of all numbers'''
                return Array(*numbers).reduce(lambda a, b, _: a+b, 0)
        >>> sums(1, 2, 3, 4)
        10
    """
    
    if not is_func(func):
        raise TypeError(f'the memoize function expected to receive a function, but received an object of type <{type(func).__name__}>')
    
    cache = {}
    
    @wraps(func)
    def wraper(*args):
        if args in cache:
            return cache[args]

        r = func(*args)
        cache[args] = r
        return r
    
    return wraper
