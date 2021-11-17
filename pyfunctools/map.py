
def map(arr:list, func) -> list:
    """Function to create a new list based on callback function return
    
    Args:
        arr ( list ) : a list to be iterated

        func ( function ) : a callback function that will be executed every iteration and should return something for reduce assemble new list.

    Examples:
        >>> map([1, 2, 3, 4], lambda item, index: item if item % 2 == 0 else None)
        [2, 4]
    """
    
    _arr = []
    
    for index in range(len(arr)):

        call = func(arr[index], index)

        if call and call != None:
            _arr.append(call)

    return _arr
