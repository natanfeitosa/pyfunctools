from pyfunctools.compact import compact

def test_compact():

    assert compact([0, 1, 2, 3, '', None, False]) == [1, 2, 3]
    assert compact([0, '', None, False]) == []
