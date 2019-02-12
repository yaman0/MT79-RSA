import math

import Tools


def chiffrement(m, n, d):
    """
    encrypt a number m with a public key (n,d)
    :param int m: number to crypt
    :param int n: n from public key
    :param int d: d from public key
    :return int : m encrypt
    """
    return Tools.modpow(m, d, n)


def dechiffrement(m, n, c):
    """
    decrypt a number m with a private key (n,c)
    :param int m: number to decrypt
    :param int n: n from private key
    :param int c: c from private key
    :return int: decrypt
    """
    return Tools.modpow(m, c, n)


def findPrivateKey(n, c):
    """
    find the private key from a public key
    :param int n: n from public key
    :param int c: d from public key
    :return int: d from public key
    """
    # Generate divisors from 2 to sqrt(n)
    divisors = [d for d in xrange(2, int(math.sqrt(n))) if n % d == 0]
    p = divisors[0]
    q = n / p
    d = Tools.inverseModulaire(c, (p - 1) * (q - 1))
    return d
