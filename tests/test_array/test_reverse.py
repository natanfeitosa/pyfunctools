from pyfunctools import Array


def test_reverse():
    
    a = Array(1, 2, 3)
    a.reverse()

    assert str(a) == '[3, 2, 1]'
