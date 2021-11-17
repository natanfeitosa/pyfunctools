from pyfunctools.filter import filter

def compact(arr: list) -> list:
    """
    Create a new list with only the truthy values from the original.

    Args:
        arr ( list ) : original list

    Return:
        list : a list with truthy values

    Examples:
        >>> compact([0, 1, 2, 3, '', None, False])
        [1, 2, 3]
        >>> compact([0, '', None, False])
        []    
    """
    return filter(arr, lambda item, _: bool(item))
