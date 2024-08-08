import time

from pyfunctools import threaded_decorator


def test_threaded_decorator():
    @threaded_decorator
    def slow_function(x):
        time.sleep(2)
        return x * 2

    result = slow_function(5)
    assert result == 10