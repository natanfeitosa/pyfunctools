import pytest
import time

from pyfunctools import timeout_decorator


def test_timeout_decorator():
    @timeout_decorator(seconds=1)
    def slow_function():
        time.sleep(2)
        return "Completed"

    with pytest.raises(TimeoutError, match="timed out after 1 seconds"):
        slow_function()
