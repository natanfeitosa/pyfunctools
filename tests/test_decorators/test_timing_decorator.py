import time

from pyfunctools import timing_decorator


def test_timing_decorator_default_logging(capfd):
    @timing_decorator()
    def example_function(x):
        time.sleep(2)
        return x * 2

    result = example_function(5)
    assert result == 10

    out, err = capfd.readouterr()
    assert "example_function took" in out


def test_timing_decorator_custom_logging(capfd):
    def custom_logger(func_name, start_time, end_time):
        duration = end_time - start_time
        print(f"{func_name} started at {start_time} and ended at {end_time}, taking {duration:.4f} seconds")

    @timing_decorator(log_func=custom_logger)
    def another_function(x):
        time.sleep(2)
        return x * 2

    result = another_function(5)
    assert result == 10

    out, err = capfd.readouterr()
    assert "another_function started at" in out
    assert "and ended at" in out
    assert "taking" in out
