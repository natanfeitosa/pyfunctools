from pyfunctools.foreach import forEach

def test_forEach():
    """Test forEach function"""
    arr = []

    def func(item, *args):
        if item % 2 == 1:
            arr.append(item)

    forEach([ 1, 2, 3, 4, 5, 6 ], func)

    assert arr == [1, 3, 5]
