from pyfunctools import Array

def test_concat():
    a = Array([])

    assert a.concat('a', ['a'], [['a']]).to_list() == ['a', 'a', ['a']]
