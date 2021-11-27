from pyfunctools import Array

def flatten(arr:list, level=1) -> list:
    """Flat list.

    Args:
        arr ( list ) : original list
        level ( int | str ) : sublist level to planar

    Note:
        Only accept whole levels or equal to 'all'

    Raises:
        ValueError : The level parameter entered is not integer or is different from 'all'

    Examples:
        >>> flatten([1, [2, [3, [4, 5]]]])
        [1, 2, [3, [4, 5]]]
        >>> flatten([1, [2, [3, [4, 5]]]], 'all')
        [1, 2, 3, 4, 5]
        >>> flatten([1, [2, [3, [4, 5]]]], 0)
        [1, [2, [3, [4, 5]]]]
    """

    if level != 'all' and not isinstance(level, int):
        raise ValueError(f'{level} is not a valid level')
    
    def func(acc, item, *kwargs):
        if Array.is_list(item) and (level == 'all' or level > 0):
            return acc.extend(flatten(item, level - 1 if isinstance(level, int) else level))
        return acc.append(item)

    return Array(arr).reduce(func, [])
