
def chunk(arr:list, size:int=1) -> list:
    """
    This function takes a list and divides it into sublists of size equal to size.

    Args:
        arr ( list ) : list to split
        size ( int, optional ) : chunk size. Defaults to 1

    Return:
        list : A new list containing the chunks of the original

    Examples:
        >>> chunk([1, 2, 3, 4])
        [[1], [2], [3], [4]]
        >>> chunk([1, 2, 3, 4], 2)
        [[1, 2], [3, 4]]
        >>> chunk([1, 2, 3, 4, 5, 6], 3)
        [[1, 2, 3], [4, 5, 6]]
    """
    _arr = []

    for i in range(0, len(arr), size):
        _arr.append(arr[i : i + size])
    
    return _arr
