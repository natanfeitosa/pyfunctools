from pyfunctools import Array


def test_pop():

    a = Array(1, 2, 3)

    assert a.pop() == 3
    assert str(a) == '[1, 2]'
