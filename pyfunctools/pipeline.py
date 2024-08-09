from pyfunctools import Array
from typing import Callable

def pipeline(*funcs: Callable) -> Callable:
    """Define a pipeline
    
    Args:
        *funcs (Callable): a variable number of callables to be called sequentially later.

    Return:
        Callable: A callable that, when invoked, executes the provided callables in sequence, 
        passing the output of each as the input to the next, 
        and returns the result of the last callable.

    Examples:
        >>> pipes = pipeline(
        ...     lambda s: s.upper(),
        ...     lambda s: s + ' 95',
        ...     lambda s: s.replace(' ', '-')
        ... )
        >>> pipes('functional python')
        'FUNCTIONAL-PYTHON-95'
        >>> pipes = pipeline(
        ...     lambda n: n + 1,
        ...     lambda x: x * 2
        ... )
        >>> pipes(1)
        4
    """
    def wrap(args):
        arr = Array(*funcs)
        return arr.reduce(lambda acc, cur, _: cur(acc), args)
    return wrap
    