from pyfunctools.utils import is_func

def test_is_func():
    def func():
        pass
    
    assert is_func(func)
    assert is_func(lambda a: a)
