import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_string_by_zero():
    assert module.rotate_string("abcdef", 0) == "abcdef"


def test_rotate_string_more_than_length():
    assert module.rotate_string("abc", 5) == "bca"