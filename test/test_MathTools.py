import pytest

from src.MathTools import *

def test_gcd_should_works():
    assert gcd(60, 48) == 12


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


def test_inverseModulaire_should_works():
    assert inverseModulaire(334, 223) == 221


def test_inverseModulaire_should_raise_exception():
    with pytest.raises(ValueError):
        inverseModulaire(2, 4)


def test_generationExposant_should_works():
    c, d = generationExposant(53, 97)
    assert c == 5
    assert d == 1997
