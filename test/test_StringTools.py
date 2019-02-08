import pytest

from src.StringTool import *

def test_stringToInt_should_works():
    assert 26943298110 == stringToInt("Bonsoir.")

def test_intToString_should_works():
    assert  "BONSOIR." == intToString(26943298110)
