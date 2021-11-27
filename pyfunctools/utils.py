from typing import Union
from re import search


NUM_RE = '([0-9])(\\.[0-9])?'

def to_num(obj: any) -> Union[int, float]:
    """Generic number converter

    Args:
        obj ( any ) : Will convert number notation to int or float

    Raises:
        ValueError : obj is not a number notation, it cannot be converted.

    Examples:
        >>> to_num('10')
        10
        >>> to_num('1.0')
        1.0
        >>> to_num('.10')
        0.1
    """

    if is_num(obj):
        if isinstance(obj, str) and obj[0] == '.':
            return float(f'0{obj}')
        elif is_float(obj):
            return float(obj)
        return int(obj)
    raise ValueError(f'{obj} is not a number notation')

def is_type(obj, name_type: str) -> bool:
    """Test custom types

    Args:
        obj ( any ) : Object to test
        name_typ ( str ) : Type name
    
    Returns :
        bool : True or False
    
    :meta private:
    """
    return str(type(obj)) == f"<class '{name_type}'>"

def is_func(obj:any) -> bool:
    """
    Tests an object and returns true if it is a function.

    Args:
        obj ( any ) : Object to test

    Examples:
        >>> is_func(lambda a: a)
        True
        >>> is_func('a')
        False
        >>> is_func(10)
        False
        >>> def func():
        ...    pass
        ...
        >>> is_func(func)
        True
    """
    return is_type(obj, 'function')

def is_int(obj: any) -> bool:
    """
    Tests an object and returns true if it is an int value.

    Args:
        obj ( any ) : Object to test

    Examples:
        >>> is_int(10)
        True
        >>> is_int(1.0)
        False
        >>> is_int(lambda a: a)
        False
        >>> is_int('a')
        False
    """
    return is_type(obj, 'int')

def is_float(obj: any) -> bool:
    """
    Tests an object and returns true if it is an int value.

    Args:
        obj ( any ) : Object to test

    Examples:
        >>> is_float(1.0)
        True
        >>> is_float(10)
        False
        >>> is_float(lambda a: a)
        False
        >>> is_float('a')
        False
    """
    m = search(NUM_RE[:-1], str(obj))
    if is_type(obj, 'float'):
        return True
    elif m and m.group(1) and len(m.group(1)) >= 1:
        return True
    return False

def is_negative(obj: Union[str, int, float]) -> bool:
    """Check if number is negative

    Examples:
        >>> is_negative('-2')
        True
        >>> is_negative('1')
        False
        >>> is_negative('1000')
        False
        >>> is_negative('-1000')
        True
    """
    return bool(search(r'(-)'+NUM_RE, str(obj)))

def is_positive(obj: Union[str, int, float]) -> bool:
    """Check if number is positive

    Examples:
        >>> is_positive('1')
        True
        >>> is_positive('1000')
        True
        >>> is_positive('-2')
        False
        >>> is_positive('-1000')
        False
    """
    return is_num(obj) and to_num(obj) > 0

def is_num(obj: any) -> bool:
    """Check if obj is number

    Examples:
        >>> is_num(10)
        True
        >>> is_num(-10)
        True
        >>> is_num(+10)
        True
        >>> is_num(.10)
        True
        >>> is_num('.10')
        True
        >>> is_num('a')
        False
    """
    return bool(is_float(obj) or is_int(obj) or search(NUM_RE, str(obj)))


def is_equal(obj1, obj2) -> bool:
    """Recursive function that checks if two parameters are equal

    Examples:
        >>> is_equal(1, 1)
        True
        >>> is_equal('{}', '{}')
        True
        >>> is_equal({}, {})
        True
        >>> is_equal([], [])
        True
        >>> is_equal({'language': 'python'}, {'language': 'python'})
        True
        >>> is_equal({'language': 'python'}, {'language': 'js'})
        False
        >>> is_equal(Array(), Array())
        True
    """
    if type(obj1) != type(obj2):
        return False
    if not is_type(obj1, 'dict') or not is_type(obj2, 'list'):
        return obj1 == obj2
    if len(obj1) != len(obj2):
        if is_type(obj1, 'list'):
            for i in range(len(obj1)):
                if not is_equal(obj1[i], obj2[i]):
                    return False
        if is_type(obj1, 'dict'):
            if len(obj1.keys()) != len(obj2.keys()):
                return False

            for k1, k2 in zip(obj1.keys(), obj2.keys()):
                if k1 != k2:
                    return False
                if not is_equal(obj1[k1], obj2[k2]):
                    return False
        if obj1 != obj2:
            return False
    return True

def is_empty(value: any) -> bool:
    """Checks if the value passed by parameter is empty.

    Examples:
        >>> is_empty('')
        True
        >>> is_empty(None)
        True
        >>> is_empty([])
        True
        >>> is_empty(Array())
        True
        >>> is_empty({})
        True
        >>> is_empty(())
        True
    """

    if value == None or not len(value) > 0:
        return True

    return True
