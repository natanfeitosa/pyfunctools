from pyfunctools import Array

def test_fill():
    a = Array(2)

    assert a.fill('a').to_list() == ['a', 'a']
