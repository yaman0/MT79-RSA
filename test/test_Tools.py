from src.Tools import *


def test_modpow_should_works():
    assert modpow(4, 13, 497) == 445

def test_euclideDiv_should_works():
    quotient, rest = euclideDiv(13, 6)
    assert quotient == 2
    assert rest == 1

def test_euclidExtend_should_works():
    pgcd, u, v = euclidExtend(135, 101)
    assert pgcd == 1
    assert u == 3
    assert v == -4

