from pyfunctools import Array


def test_append():
    array = Array(1, 2, 3)
    array.append(4)

    assert str(array) == '[1, 2, 3, 4]'
