from re import sub
from .reduce import reduce

def at(obj:dict, path:str) -> any:
    """Returns the value corresponding to path in obj

    Args:
        obj ( dict ) : The dictionary we want to get the value from

        path ( str ) : The path of the value that should be returned

    Examples:
        >>> obj = { 'a': 1, 'b': { 'a': 1, 'b': [ 'a' ] } }
        >>> at(obj, 'a')
        1
        >>> at(obj, 'b.a')
        1
        >>> at(obj, 'b.b')
        [ 'a' ]
        >>> at(obj, 'b.b.0')
        'a'
        >>> at(obj, 'b.b[0]')
        'a'
    """

    def repl(match):

        _format = lambda text: text.replace('[', '').replace(']', '')

        if match.groups('s1'):
            return _format(match.group('s1') + '.' + match.group('s2'))

        return _format(match.group('s2'))

    paths = sub(
        r'((?P<s1>[a-z])?(?P<s2>\[\d\]))',
        repl,
        path
    ).split('.')

    def func(acc, item, *kwargs):

        if item.isnumeric():
            return acc[int(item)]
        
        return acc[item]

    return reduce(paths, func, obj)
    