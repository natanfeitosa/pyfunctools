def test_flat_map():
    func1 = lambda x, *args: [x, x * 2]
    assert flat_map([1, 2, 3], func1) == [1, 2, 2, 4, 3, 6]

    func2 = lambda x, *args: [x] if x % 2 == 0 else []
    assert flat_map([1, 2, 3, 4], func2) == [2, 4]

    func3 = lambda x, *args: x * 2 if x % 2 == 0 else [x, x + 1]
    assert flat_map([1, 2, 3, 4], func3) == [1, 2, 4, 3, 4, 4]