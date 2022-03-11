import time
from pyfunctools import Array
from pyfunctools.memoize import memoize

def perc(fn, *args):
    start = time.time()
    res = fn(*args)
    end = time.time()

    return res, end - start

def test_memoize():
    fat = memoize(lambda n: 1 if n == 0 else n * fat(n-1))
    fr1, tf1 = perc(fat, 4)
    fr2, tf2 = perc(fat, 4)
    assert fr1 == fr2 and tf1 >= tf2

    @memoize
    def sums(*numbers):
        return Array(*numbers).reduce(lambda a, b, _: a+b, 0)

    sr1, t1 = perc(sums, 1, 22, 333, 4444, 55555, 666666)
    sr2, t2 = perc(sums, 1, 22, 333, 4444, 55555, 666666)

    assert sr1 == sr2 and t1 >= t2

    try:
        memoize({})
    except:
        assert True
    else:
        assert False

    try:
        @memoize
        class Noop:
            pass

        Noop()
    except:
        assert True
