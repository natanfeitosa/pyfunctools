from pyfunctools.filter import filter

def test_filter():
    func = lambda item, *args: item % 2 == 0

    assert filter([1, 2, 3, 4], func) == [2, 4]
