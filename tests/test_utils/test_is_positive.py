from pyfunctools.utils import is_positive

def test_is_positive():

    assert is_positive(1.0)
    assert is_positive(+10)
    assert is_positive(10000)
    assert is_positive('100')
    assert not is_positive(-100)
    assert not is_positive('-100')
    assert not is_positive('-1.0')
    assert not is_positive('a')
