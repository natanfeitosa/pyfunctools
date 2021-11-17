
def forEach(arr:list, func):
    """Iterates over a list and calls a function for each item, passing the item itself and the index

    Args:
        arr ( list ) : List to iterate
        func ( function ) : Callback function

    Examples:
        >>> forEach([1, 2], lambda item, index: print(f'{item}, {index}'))
        1, 0
        2, 1
    """

    for index in range(len(arr)):
        
        func(arr[index], index)
