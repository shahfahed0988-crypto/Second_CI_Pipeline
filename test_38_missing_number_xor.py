import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_number():
    assert module.missing_number([3, 0, 1]) == 2


def test_missing_number_another():
    assert module.missing_number([0, 1, 2, 4, 5]) == 3


def test_missing_zero():
    assert module.missing_number([1, 2, 3]) == 0