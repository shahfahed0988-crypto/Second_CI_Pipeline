import importlib

module = importlib.import_module("40_gcd")


def test_gcd():
    assert module.gcd(48, 18) == 6


def test_gcd_another():
    assert module.gcd(20, 8) == 4


def test_gcd_with_one():
    assert module.gcd(17, 1) == 1