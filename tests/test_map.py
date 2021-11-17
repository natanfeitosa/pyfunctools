from pyfunctools.map import map


def test_map():
    func = lambda item, *args: item if item % 2 == 0 else None

    assert map([1, 2, 3, 4], func) == [2, 4]
