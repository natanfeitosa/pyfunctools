from pyfunctools.utils import is_float

def test_is_float():

    assert is_float(1.0)
    assert not is_float(10000)
    assert not is_float('a')
