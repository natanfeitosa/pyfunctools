
def reduce(arr:list, func, initial:any=[]):
    """Function to create a new object based on callback function return
    
    Args:
        arr ( list ) : A list to be iterated
        func ( function ) : A callback function that will be executed every iteration and should return something for reduce assemble new object
        initial ( any, [] ) : Initial return value.

    Raises:
        NotImplementedError:
            Arr or func not defined or equal to None.

    Examples:
        >>> arr = [1, 2, 3, 4, 5, 6]
        >>> def func(accumulator, item, index):
        ...     if item % 2 == 0:
        ...         return accumulator.append(item)
        ...     return
        ...
        >>> reduce(arr, func)
        [2, 4, 6]
    
    Note:
        if the callback function never returns anything, reduce will return the initial value itself
    """

    if arr == None:
        raise NotImplementedError('arr cannot be None.')
    if func == None:
        raise NotImplementedError('func cannot be None.')
  
    acc = initial

    for index in range(len(arr)):
        
        call = func(acc, arr[index], index)

        if call and call != None:
            acc = call

    return acc
