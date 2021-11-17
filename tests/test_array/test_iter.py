from pyfunctools import Array

def test_iter():
    assert [
        i
        for i in Array(1, 2, 3)
        if i % 2 == 0
    ] == [ 2 ]
