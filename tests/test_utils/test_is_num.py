from pyfunctools.utils import is_num

def test_is_num():

    assert is_num(1.00)
    assert is_num(1000)
    assert is_num('10')
    assert is_num('-1')
    assert not is_num('a')
