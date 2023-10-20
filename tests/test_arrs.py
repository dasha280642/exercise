
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.get([], 1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

import pytest

def test_my_slice_empty_list():
    assert arrs.my_slice([], 0, 2) == []

def test_my_slice_no_start_no_end():
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_my_slice_start_only():
    assert arrs.my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]

def test_my_slice_start_negative():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]

def test_my_slice_end_only():
    assert arrs.my_slice([1, 2, 3, 4, 5], end=3) == [1, 2, 3]

def test_my_slice_end_negative():
    assert arrs.my_slice([1, 2, 3, 4, 5], end=-2) == [1, 2, 3]

def test_my_slice_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]

def test_my_slice_start_and_end_negative():
    assert arrs.my_slice([1, 2, 3, 4, 5], -4, -1) == [2, 3, 4]

def test_my_slice_start_and_end_out_of_range():
    assert arrs.my_slice([1, 2, 3, 4, 5], 10, 20) == []

def test_my_slice_start_and_end_negative_out_of_range():
    assert arrs.my_slice([1, 2, 3, 4, 5], -10, -20) == []
