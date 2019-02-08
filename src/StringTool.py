import math

import Tools

alphabet = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
size = len(alphabet)


def stringToInt(string):
    number = 0
    for i in range(0, len(string)):
        c = string[i]
        alphabetIndex = alphabet.find(str.upper(c))
        number += math.pow(size, len(string) - 1 - i) * alphabetIndex
    return int(number)


def intToString(number):
    #init
    string = ""
    q, r = Tools.euclideDiv(number, size)

    while q % size > 0:
        string = alphabet[r] + string
        q, r = Tools.euclideDiv(q, size)

    string = alphabet[r] + string
    return string
