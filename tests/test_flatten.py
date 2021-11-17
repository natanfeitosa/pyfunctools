from pyfunctools.flatten import flatten

def test_flatten():
    original_array = [1, [2, [3, [4, 5]]]]

    call = flatten(original_array)

    assert call != original_array
    assert call == [1, 2, [3, [4, 5]]]
    assert flatten(original_array, 'all') == [1, 2, 3, 4, 5]
    assert flatten(original_array, 0) == original_array
