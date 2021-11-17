from pyfunctools import Array

def test_map():
    a = Array(1, 2, 3, 4)

    func = lambda item, *args: item if item % 2 == 0 else None
    
    assert a.map(func) == [2, 4]
