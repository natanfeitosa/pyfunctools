from pyfunctools import Array


def test_index_of():
    
    a = Array(1, 2, 3, 4)

    assert a.index_of(1) == 0
    assert a.index_of(2) == 1
    assert a.index_of(3) == 2
    assert a.index_of(4) == 3
    assert a.index_of(5) == -1
