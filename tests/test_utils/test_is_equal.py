from pyfunctools import Array
from pyfunctools.utils import is_equal

def test_is_equal():

    assert is_equal(1, 1)
    assert is_equal('{}', '{}')
    assert is_equal({}, {})
    assert is_equal([], [])
    assert is_equal({'language': 'python'}, {'language': 'python'})
    assert not is_equal({'language': 'python'}, {'language': 'js'})
    assert is_equal(Array(), Array())
