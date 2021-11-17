from pyfunctools import Array

def test_setitem():

    a = Array(1)

    try:
        a[1]
    except IndexError:
        assert True

    assert a[0] == None
