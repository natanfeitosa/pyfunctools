from pyfunctools import Array


def test_includes():
    a = Array(1, 2)

    assert a.includes(2)
    assert not a.includes(3)
