"""
Pyfunctools
======

Pyfunctools is a module that provides functions, methods and classes that help in the creation of projects in python, bringing functional and object-oriented programming methods.
"""

MAJOR = 0
MINOR = 4
PATCH = 1

def get_version(release:bool=False):
    """Get simple version or full version/release of pyfunc

    Args:
        release ( bool, False ) : if true, return full version of package

    Examples:
        >>> get_version()
        '0.1'
        >>> get_version(True)
        '0.1.0'
    """

    version = f'{MAJOR}.{MINOR}'

    if release:
        return f'{version}.{PATCH}'

    return version

from typing import List

from .chunk import chunk
from .filter import filter
from .foreach import forEach
from .map import map
from .reduce import reduce
from .utils import is_equal


class Array(object):
    """Class that has common methods in arrays that are not present in the builtin list class.

    Raises:
        NotImplementedError: Error thrown when a None value is passed in the constructor
    
    Examples:
        >>> #Create an array/list 
        >>> Array()
        <Array values=[] >
        >>> Array(4)
        <Array values=[None, None, None, None] >
        >>> Array(1, 2)
        <Array values=[1, 2] >
    """

    @staticmethod
    def is_list(arr: any) -> bool:
        """Test an object and return true if it is an instance of list

        Examples:
            >>> Array.is_list([])
            True
            >>> Array.is_list({})
            False
        """
        return isinstance(arr, list)
    
    @staticmethod
    def is_array(arr: any) -> bool:
        """Test an object and return true if it is an instance of Array

        Examples:
            >>> array = Array()
            >>> Array.is_list(array)
            True
            >>> Array.is_list({})
            False
        """
        return isinstance(arr, Array)
    
    def __init__(self, *args, default=None):
        
        if len(args) == 1:
            if args[0] == None and default == None:
                raise NotImplementedError('No parameters')

            elif isinstance(args[0], list):
                self._values = args[0]
            else:
                self._values = [default] * args[0]
        else:
            self._values = list(args)

    def __str__(self) -> str:
        return str(self._values)

    def __repr__(self) -> str:
        repr = '<Array values={} >'
        return repr.format(self)

    def __eq__(self, other):
        if not Array.is_array(other):
            return False
        return is_equal(self.to_list(), other.to_list())

    def __getitem__(self, index):
        return self._values.__getitem__(index)

    def __setitem__(self, index, value):
        if index < len(self):
            self._values.__setitem__(index, value)
            return
        elif index == len(self) + 1:
            self._values.append(value)
            return

        raise IndexError('array assignment index out of range')

    def __len__(self) -> int:
        return self._values.__len__()

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n < len(self):
            result = self[self._n]
            self._n += 1
            return result
        else:
            raise StopIteration
    
    def append(self, x:any):
        """Append a new item with value x to the end of the Array.

        Args:
            x ( any ) : object to add

        Examples:
            >>> array = Array(1, 2, 3)
            >>> array.append(4)
            >>> array.to_list()
            [1, 2, 3, 4]
        """
        return self._values.append(x)

    def chunk(self, size:int=1) -> List[list]:
        """Divides the Array object into sublists.

        Args:
            size ( int, optional ) : Chunk size. Defaults to 1

        Return:
            list : A new list containing the chunks of the Array object

        Examples:
            >>> array = Aray([1, 2, 3, 4])
            >>> array.chunk()
            [[1], [2], [3], [4]]
            >>> array.chunk(2)
            [[1, 2], [3, 4]]
            >>> array.chunk(3)
            [[1, 2, 3], [4, 5, 6]]
        """
        return chunk(self._values, size)
    
    def clone(self):
        """Clone this array instance

        Returns:
            Array : A new array
        """
        return Array(*self)

    def concat(self, *args):
        """Concatenate into Array

        Returns:
            Array : The Array instance being changed
        
        Examples:
            >>> a = Array([1, 2])
            >>> a.concat(3)
            <Array values=[1, 2, 3] >
            >>> a.concat([4, 5], [6, 7])
            <Array values=[1, 2, 3, 4, 5, 6, 7] >
            >>> #Turning into list type
            >>> a.to_list()
            [1, 2, 3, 4, 5, 6, 7]
        """

        for i in args:
            if isinstance(i, list):
                self._values.extend(i)
                continue
            self._values.append(i)
        
        return self
    
    def count(self, x:any) -> int:
        """Return the number of times x appears in the array.
        
        Examples:
            >>> Array(1, 2, 3).count(1)
            1
            >>> Array(2, 0, 2, 2).count(2)
            3
            >>> Array(2, 0, 0, 2).count(1)
            0
        """

        return self._values.count(x)

    def fill(self, fill_with:any):
        """Replaces/fill the values in the array without changing the len

        Returns:
            Array : The Array instance being changed
        
        Examples:
            >>> a = Array([1, 2])
            >>> a.fill('a')
            <Array values=['a', 'a'] >
            >>> #Turning into list type
            >>> a.to_list()
            ['a', 'a']
        """
        _arr = []
        for _ in range(len(self)):
            _arr.append(fill_with)
        
        self._values = _arr
        return self

    def filter(self, func) -> list:
        """Method to filter a Aray item
        
        Args:
            func ( function ) : The callback function takes an item and index, and must return a boolean

        Examples:
            >>> array = Array(1, 2, 3, 4)
            >>> array.filter(lambda item, index: item % 2 == 0)
            [2, 4]
        """
        return filter(self, func)
    
    def forEach(self, func):
        """Calls a function for each item, passing the item itself and the index

        Args:
            func ( function ) : Callback function

        Examples:
            >>> array = Array(1, 2)
            >>> array.forEach(lambda item, index: print(f'{item}, {index}'))
            1, 0
            2, 1
        """
        return forEach(self, func)

    def includes(self, item:any) -> bool:
        """Test if an item exists in this Array

        Args:
            item ( any ) : Item to test

        Examples:
            >>> array = Array(1, 2, 3)
            >>> array.includes(4)
            False
            >>> array.includes(1)
            True
        """
        return item in self._values
    
    def index_of(self, obj: any) -> int:
        """The method returns the first index at which a given element can be found in the array, or -1 if it is not present.

        Args:
            obj ( any ) : Element to locate in the array.
        
        Returns:
            int : -1 if not exists in the array
        
        Examples:
            >>> array = Array(1, 2, 3)
            >>> array.index_of(4)
            -1
            >>> array.index_of(1)
            0
        """
        if self.includes(obj):
            return self._values.index(obj)
        return -1

    def map(self, func) -> list:
        """Function to create a new list based on callback function return
        
        Args:
            func ( function ) : A callback function that will be executed every iteration and should return something for reduce assemble new list.

        Examples:
            >>> array = Array([1, 2, 3, 4])
            >>> array.map(lambda item, index: item if item % 2 == 0 else None)
            [2, 4]
        """
        return map(self, func)
    
    def pop(self, pos:int=-1) -> any:
        """Removes the element at the specified position.

        Args:
            pos ( int, -1 ) : Position of the element to be removed and returned.
        
        Examples:
            >>> array = Array(1, 2, 3)
            >>> array.pop()
            3
            >>> array.pop(0)
            1
            >>> array
            <Array values=[2] >
        """
        return self._values.pop(pos)

    def reduce(self, func, initial=[]):
        """Function to create a new object based on callback function return
        
        Args:
            func ( function ) : A callback function that will be executed every iteration and should return something for reduce assemble new object
            initial ( any, [] ) : Initial return value.

        Raises:
            NotImplementedError:
                func not defined or equal to None.

        Examples:
            >>> array = Array([1, 2, 3, 4, 5, 6])
            >>> def func(accumulator, item, index):
            ...     if item % 2 == 0:
            ...         return accumulator.append(item)
            ...     return
            ...
            >>> array.reduce(func)
            [2, 4, 6]
        
        Note:
            if the callback function never returns anything, reduce will return the initial value itself
        """
        return reduce(self, func, initial)
    
    def repetitions(self) -> dict:
        """Parses and returns all repetitions in the array.

        Returns:
            dict : A dictionary of type item: int(repetitions)
        
        Examples:
            >>> Array(*'Pyfunctools').repetitions()
            {"P": 1, "y": 1, "f": 1, "u": 1, "n": 1, "c": 1, "t": 1, "o": 2, "l": 1, "s": 1}
            >>> Array(*'Python').repetitions()
            {"P": 1, "y": 1, "t": 1, "h": 1, "o": 1, "n": 1}
        """
        def func(acc, item, _):
            try:
                _n = acc[item]
            except:
                _n = 0
            acc[item] = _n + 1
            return acc

        return self.reduce(func, {})

    def reverse(self):
        """Reverses the sorting order of the elements.

        Examples:
            >>> array = Array(1, 2, 3)
            >>> array.reverse()
            >>> array
            <Array values=[3, 2, 1] >
        """
        return self._values.reverse()
    
    def shift(self):
        """Removes the first element from an array and returns that removed element.

        Examples:
            >>> array = Array(1, 2, 3)
            >>> array.shift()
            1
            >>> array
            <Array values=[2, 3] >
            >>> array.shift()
            2
            >>> array
            <Array values=[3] >
        """
        return self.pop(0)

    def to_list(self) -> list:
        """Convert the array object to the builtin type list.

        Note:
            If you prefer you can use list compression on the Array instance
        """
        return list(self)

    def unshift(self, *args):
        """Adds one or more elements to the beginning of an array and returns a array modified."""
        _args = [a for a in args]

        self._values = [
            *_args,
            *self._values
        ]

        return self
