def flat_map(arr: list, func) -> list:
    """Applies a function to each element in the list and flattens the result
    Args:
        arr (list): a list to iterate
        func (function): a callback function that returns a list for each element
    Examples:
        >>> numbers = [1, 2, 3, 4]
        >>> flat_map(numbers, lambda x: [x, x * 2])
        [1, 2, 2, 4, 3, 6, 4, 8]
    """
    result = []
    for index, item in enumerate(arr):
        mapped = func(item, index)
        if isinstance(mapped, list):
            result.extend(mapped)
        else:
            result.append(mapped)
    return result