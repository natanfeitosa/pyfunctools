from pyfunctools import Array

def test_is_empty():

    assert Array().is_empty()
    assert not Array(1, 2).is_empty()
