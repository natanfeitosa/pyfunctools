from pyfunctools.chunk import chunk

def test_chunk():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
