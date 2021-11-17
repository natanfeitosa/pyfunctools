from pyfunctools import Array

def test_setitem():

    a = Array(1)

    try:
        a[2] = '1'
    except IndexError:
        assert True

    a[1] = 1

    assert a.to_list() == [None, 1]
