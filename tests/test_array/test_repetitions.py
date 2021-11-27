from pyfunctools import Array
from pyfunctools.utils import is_equal


def test_repetitions():
    
    a = Array(*'Pyfunctools')

    assert is_equal(
        a.repetitions(),
        {
            "P": 1,
            "y": 1,
            "f": 1,
            "u": 1,
            "n": 1,
            "c": 1,
            "t": 1,
            "o": 2,
            "l": 1,
            "s": 1
        }
    )
