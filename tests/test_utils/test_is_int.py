from pyfunctools.utils import is_int

def test_is_int():

    assert is_int(10000)
    assert not is_int('a')
    assert not is_int(1.0)
