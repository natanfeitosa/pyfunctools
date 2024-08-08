import pytest

from pyfunctools import retry_decorator


def test_retry_decorator_success():
    @retry_decorator(retries=5, delay=1)
    def flaky_function():
        if not hasattr(flaky_function, "attempts"):
            flaky_function.attempts = 0
        flaky_function.attempts += 1
        if flaky_function.attempts < 3:
            raise ValueError("Oops, something went wrong!")
        return "Success!"

    result = flaky_function()
    assert result == "Success!"


def test_retry_decorator_failure():
    @retry_decorator(retries=3, delay=1)
    def always_fails():
        raise ValueError("This function always fails!")

    with pytest.raises(ValueError, match="This function always fails!"):
        always_fails()