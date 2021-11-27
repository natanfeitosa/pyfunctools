from pyfunctools import Array


def test_shift():
    
    a = Array(1, 2, 3)

    assert a.shift() == 1
    assert a.shift() == 2
