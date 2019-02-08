import pytest

from src.RSA import *


def test_chiffrement_should_work():
    assert chiffrement(123, 221, 5) == 106

def test_dechiffrement_should_work():
    assert dechiffrement(106, 221, 1997) == 123
