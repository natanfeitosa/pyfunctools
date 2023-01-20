from pyfunctools import Array

def pipeline(*funcs):
    """Define a pipeline
    
    Args:
        *funcs ( list[callable] ) : a list of callables to be called later

    Return:
        last pipe return

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
    