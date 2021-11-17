from pyfunctools.utils import is_negative

def test_is_negative():

    assert is_negative(-1000)
    assert is_negative('-100')
    assert is_negative('-1.0')
    assert not is_negative(1.0)
    assert not is_negative(+10)
    assert not is_negative(10000)
    assert not is_negative('100')
    assert not is_negative('a')
