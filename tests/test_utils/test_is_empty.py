from pyfunctools import Array
from pyfunctools.utils import is_empty

def test_is_empty():

    assert is_empty('')
    assert is_empty(None)
    assert is_empty([])
    assert is_empty(Array())
    assert is_empty({})
    assert is_empty(())
