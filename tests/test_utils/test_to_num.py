from pyfunctools.utils import to_num

def test_to_num():
    assert to_num('.2') == 0.2
    assert to_num('0.2') == 0.2
    assert to_num('2') == 2
    assert to_num('-2') == -2
