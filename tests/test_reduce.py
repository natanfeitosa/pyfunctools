from pyfunctools.reduce import reduce

def test_reduce():
    """Test reduce function"""
    arr = [ 1, 2, 3, 4, 5, 6 ]

    func = lambda acc, item, *kwargs: acc.append(item) if item % 2 == 0 else acc

    assert reduce(arr, func, list()) == [ 2, 4, 6 ]
