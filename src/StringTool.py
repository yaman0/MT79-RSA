import math

import MathTools

# constants
ALPHABET = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SIZE = len(ALPHABET)


def stringToInt(string):
    """
    transform a string to a number
    :param str string: string to convert
    :return int: the conversion
    """
    number = 0
    for i in range(0, len(string)):
        c = string[i]
        alphabetIndex = ALPHABET.find(str.upper(c))
        number += math.pow(SIZE, len(string) - 1 - i) * alphabetIndex
    return int(number)


def intToString(number):
    """
    transform a number to a string
    :param int number: number to convert
    :return str: conversion
    """
    #init
    string = ""
    q, r = MathTools.euclideDiv(number, SIZE)

    while q % SIZE > 0:
        string = ALPHABET[r] + string
        q, r = MathTools.euclideDiv(q, SIZE)

    string = ALPHABET[r] + string
    return string
