from pyfunctools import Array


def test_count():
    a = Array(*'Pyfunctools')

    assert a.count('a') == 0
    assert a.count('s') == 1
    assert a.count('o') == 2
