_1stN = __import__("1stN_v1")

def test_ok_contiguous_arrays():
    assert _1stN.operations_to_permutation([1, 2, 3, 4]) == 0
    assert _1stN.operations_to_permutation([2, 3, 4, 5]) == 4
    assert _1stN.operations_to_permutation([4, 3, 2, 1]) == 0

def test_ok_non_contiguous_arrays():
    assert _1stN.operations_to_permutation([1, 2, 3, 5]) == 1
    assert _1stN.operations_to_permutation([2, 3, 4, 5]) == 4
    assert _1stN.operations_to_permutation([1, 3, 5, 7]) == 6
    assert _1stN.operations_to_permutation([2, 4, 6, 8]) == 10

