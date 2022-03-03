from pyfunctools import Array


def test_append():
    array1 = Array(1, 2, 3)
    array2 = array1.clone()

    assert array1 == array2
