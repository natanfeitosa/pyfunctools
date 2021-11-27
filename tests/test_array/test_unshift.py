from pyfunctools import Array


def test_unshift():
    
    a = Array(2, 3)
    
    assert str(a.unshift(1)) == '[1, 2, 3]'
    assert str(a.unshift(0)) == '[0, 1, 2, 3]'
    assert str(a.unshift(10)) == '[10, 0, 1, 2, 3]'
    